# 마을의 시장직을 맡고있는 코디는 밤거리가 너무 어둡다는 민원을 받아 거리에 가로등을 추가, 조정하려 합니다.
# 마을의 거리는 1부터 N까지의 직선 좌표로 표현됩니다. 모든 가로등은 동일한 소비 전력(r)을 사용하며, 각 가로등은 설치된 위치 x를 기준으로 구간 [x−r,x+r] 거리를 밝힙니다.
# 코디는 다음과 같은 작업들을 명령할 수 있습니다.
# 마을 상태 확인
# N: 거리의 크기 (좌표 1부터 N까지 존재)
# M: 초기에 존재하는 가로등의 개수
#  : 초기에 존재하는 각 가로등의 위치 정보
# 가로등은 좌표 오름차순으로 주어지며, 주어진 순서대로 1,2,⋯,M번의고유 번호가 부여됩니다
#모든 가로등은 동일한 소비 전력(r)을 사용한다.
import sys
import heapq

input = sys.stdin.readline
def ceil_half(x):
    # x / 2를 올림한 값
    # 200번에서 새 가로등 위치를 구할 때 사용
    return (x + 1) // 2

def solution():
    # Q는 그냥 인풋된대로 받으면 됨.
    Q = int(input())
    pos = {} # 가로등 번호 -> 위치
    prev = {} #왼쪽 이웃 가로등 번호
    nxt = {} #오른쪽 이웃 가로등 번호
    alive = set() #현재 살아있는 가로등 번호들
    # 인접한 두 가로등 사이의 gap을 저장하는 heap
    # 파이썬 heapq는 최소 힙이라서, 최대 gap을 꺼내기 위해 -gap으로 저장
    gap_heap = []
    head = None #가장 왼족 가로등 번호
    tail = None #가장 오른쪽 가로등 번호
    next_id = 1 #새로 추가될 가로등 번호
    answer = [] #400번 명령 결과 저장

    def push_gap(left, right):
        # left와 right는 현재 인접한 두 가로등 번호
        gap = pos[right] - pos[left]
        # -gap: 최대 gap을 먼저 꺼내기 위해 음수로 저장
        # pos[left]: gap이 같을 때 더 왼쪽 구간을 먼저 고르기 위한 값. 그 번호의 가로등의 위치.
        # left, right: 나중에 이 구간이 아직 유효한지 검사하기 위해 저장
        #heapq.heappush(힙리스트, 넣을값) . 정확히는 튜플로 넣음.
        heapq.heappush(gap_heap, (-gap, pos[left], left, right))
    def get_valid_max_gap():
        # heap top이 현재도 유효한 gap인지 확인한다.
        # 유효하지 않은 옛날 gap일 때만 heap에서 제거한다.
        while gap_heap:
            #heap top을 확인함.
            neg_gap, _, left, right = gap_heap[0] # 꺼내지 않고 보기만 함
            gap = -neg_gap
            # 둘 중 하나라도 삭제된 가로등이면 옛날 gap
            if left not in alive or right not in alive:
                #heap에서 제거
                heapq.heappop(gap_heap)
                continue
            # left의 현재 오른쪽 이웃이 right가 아니면 옛날 gap
            if nxt[left] != right:
                #heap에서 제거함. 이미 끊어진 옛날 구간이므로.
                heapq.heappop(gap_heap)
                continue
            ## 여기까지 통과하면 현재도 유효한 최대 gap
            return gap, left, right
        #heap이 비어 있거나 유효한 gap이 없으면
        return 0, None, None

    # 두번째 줄. Q=2일때.
    for _ in range(Q):
        query = list(map(int, input().split()))
        action = query[0]
        # 0번 인덱스가 실험명령의 형식.
        # 200: 가로등을 추가함.
        if action == 100:
            N = query[1]
            M = query[2]
            # 복잡하니까 아예 가로등 번호랑, 위치랑 따로 떼려고 이렇게 변수정의를 함.
            # 초기 가로등 위치 리스트.
            positions = query[3:]
            #인접한 가로등 사이의 거리를 알아냄.
            # 인접한 가로등 사이의 거리를 알아내는 방법은
            # 초기 가로등은 주어진 순서대로 1번부터 M번까지 번호를 가진다.
            # positions는 리스트라서 인덱스가 0부터 시작한다.
            # 하지만 가로등 번호는 1부터 시작한다.
            for i in range(M):
                light_id = i + 1
                # 딕셔너리에 번호를 넣으면 가로등 위치가 저장되도록 함.
                pos[light_id] = positions[i]
                #alive에 id추가
                alive.add(light_id)
            # 이중 연결 리스트 만들기
            # 1번 --- 2번 --- 3번 --- ... --- M번
            # 가로등 번호 1번부터 M번까지 모두 prev/nxt를 만든다.
            # range(1, M + 1)은 1, 2, ..., M까지 돈다.
            for i in range(1, M+1):
                prev[i] = i -1
                nxt[i] = i +1
            # 1번은 가장 왼쪽이라 왼쪽 이웃이 없다.
            prev[1] = None
            # M번은 가장 오른쪽이라 오른쪽 이웃이 없다.
            nxt[M] = None

            head = 1
            tail = M
            # 다음 가로등 번호는 이렇게 정의함.
            next_id = M +1
            # 초기 인접 gap을 heap에 넣는다.
            # 인접 gap은 1-2, 2-3, ..., M-1번과 M번 사이에만 있다.
            # 그래서 i는 1부터 M-1까지만 돈다.
            for i in range(1, M):
                push_gap(i, i +1)
        #200번 가로등 추가.
        elif action == 200:
            # 현재 가장 큰 유효 gap을 꺼낸다
            #max_gap을 아예 정의를 하려고 함.
            _, left, right = get_valid_max_gap()
            # left와 right 사이의 가운데에 새 가로등을 설치한다.
            # 문제에서 나누어떨어지지 않으면 올림이라고 했으므로 ceil_half 사용
            new_pos = ceil_half(pos[left] + pos[right])
            new_id = next_id
            next_id += 1
            # 새 가로등 번호와 위치 저장.
            pos[new_id] = new_pos
            alive.add(new_id)
            # 기존 연결:
            # left --- right
            #
            # 새 연결:
            # left --- new_id --- right
            #새 id의 입장을 생각하기.
            prev[new_id] = left  # new_id의 왼쪽은 left
            nxt[new_id] = right  # new_id의 오른쪽은 right
            #기존 가로등 입장도 생각하기.
            nxt[left] = new_id  # left의 오른쪽은 new_id
            prev[right] = new_id  # right의 왼쪽은 new_id
            # 새로 생긴 인접 gap 두 개를 heap에 넣는다.
            push_gap(left, new_id)
            push_gap(new_id, right)


        #300번은 D번 가로등을 제거함.
        elif action == 300:
            D = query[1]
            # 이미 삭제된 가로등이면 무시
            if D not in alive:
                continue

            left = prev[D]
            right = nxt[D]

            #D번 가로등 삭제 처리. set이라 del로 안됨.
            alive.remove(D)
            # # D의 왼쪽 이웃이 있으면, 그 이웃의 오른쪽을 right로 바꾼다.
            if left is not None:
                nxt[left] = right
            # D의 오른쪽 이웃이 있으면
            if right is not None:
                prev[right] = left
            #D가 가장 왼쪽 가로등이었다면 head갱신
            if D == head:
                head = right
            #D가 가장 오른쪽 가로등이었다면 tail갱신
            if D == tail:
                tail = left
            #D가 중간 가로등이었단면 left와 right가 새로 인접하게 된다.
            if left is not None and right is not None:
                push_gap(left, right)
        # 400: 최적위치 계산.
        elif action == 400:
            max_gap, _, _ = get_valid_max_gap()
            # 왼쪽 끝 1부터 첫 번째 가로등까지는 head 가로등 혼자 밝혀야 한다.
            # 필요한 r = pos[head] - 1
            # 문제는 2r을 출력하므로 후보는 2 * (pos[head] - 1)
            left_candidate = 2 * (pos[head] -1)
            # 마지막 가로등부터 오른쪽 끝 N까지는 tail 가로등 혼자 밝혀야 한다.
            # 필요한 r = N - pos[tail]
            # 출력은 2r이므로 후보는 2 * (N - pos[tail])
            right_candidate = 2 * (N - pos[tail])
            # 인접한 두 가로등 사이는 양쪽 가로등이 같이 밝힌다.
            # 두 가로등 사이 거리 gap에 대해 r + r >= gap
            # 즉 2r >= gap
            # 그래서 후보는 max_gap 자체다.
            middle_candidate = max_gap
            double_r = max(left_candidate, right_candidate, middle_candidate)
            answer.append(str(double_r))
    print("\n".join(answer))
solution()