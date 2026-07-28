# 마을의 시장직을 맡고있는 코디는 밤거리가 너무 어둡다는 민원을 받아 거리에 가로등을 추가, 조정하려 합니다.
# 마을의 거리는 1부터 N까지의 직선 좌표로 표현됩니다. 모든 가로등은 동일한 소비 전력(r)을 사용하며, 각 가로등은 설치된 위치 x를 기준으로 구간 [x−r,x+r] 거리를 밝힙니다.
# 코디는 다음과 같은 작업들을 명령할 수 있습니다.
# 마을 상태 확인
# N: 거리의 크기 (좌표 1부터 N까지 존재)
# M: 초기에 존재하는 가로등의 개수
#  : 초기에 존재하는 각 가로등의 위치 정보
# 가로등은 좌표 오름차순으로 주어지며, 주어진 순서대로 1,2,⋯,M번의고유 번호가 부여됩니다
#모든 가로등은 동일한 소비 전력(r)을 사용한다.
def solution():
    # Q는 그냥 인풋된대로 받으면 됨.
    Q = int(input())
    lights = {} # 가로등 번호 -> 위치
    positions = [] #현재 살아있는 가로등 위치들
    next_id = 1 #새 가로등 번호
    N = 0
    M = 0

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
            positions = query[3:]
            #인접한 가로등 사이의 거리를 알아냄.
            # 인접한 가로등 사이의 거리를 알아내는 방법은
            for i in range(M):
                # lights 딕셔너리에 번호를 넣으면 가로등 위치가 저장되도록 함.
                lights[i+1] = positions[i]
            # 다음 가로등 번호는 이렇게 정의함.
            next_id = M +1
        #200번 가로등 추가.
        elif action == 200:
            positions.sort()
            #max_gap을 아예 정의를 하려고 함.
            max_gap = -1
            target_idx = -1
            #인접한 가로등 사이 거리 중 가장 큰 구간 찾기
            for i in range(len(positions) -1):
                gap = positions[i+1] - positions[i]
                if gap > max_gap:
                    max_gap = gap
                    target_idx = i
            left = positions[target_idx]
            right = positions[target_idx+1]
            #새로운 가로등# (left + right) / 2 를 올림한 위치
            new_pos = (left + right+1) //2
            lights[next_id] = new_pos
            positions.append(new_pos)
            next_id += 1


        #300번은 D번 가로등을 제거함.
        elif action == 300:
            D = query[1]
            if D in lights:
                remove_pose = lights[D]
                # 실제로 삭제하는 명령어
                del lights[D]
                positions.remove(remove_pose)

        # 400: 최적위치 계산.
        elif action == 400:
            positions.sort()
            #double_r는 왼쪽 끝을 밝히는 데 필요한 2r,
            # 오른쪽 끝을 밝히는 데 필요한 2r,
            # 그리고 인접한 가로등 사이 gap들을 하나씩 보면서
            # 그중 가장 큰 값을 저장하는 변수다.
            double_r = 0
            #왼쪽 끝 1까지 밝히기
            double_r = max(double_r, 2 * (positions[0] -1))
            # 오른쪽 끝 N까지 밝히기
            double_r = max(double_r, 2 * (N - positions[-1]))
            #인접한 가로등 사이 밝히기
            for i in range(len(positions)-1):
                gap = positions[i+1] - positions[i]
                double_r = max(double_r, gap)
            print(double_r)
solution()