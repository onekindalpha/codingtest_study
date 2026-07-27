#좌측 하단의 좌표는 (0, 0), 가장 우측 상단의 좌표는 (N, N)\
#Q번의 실험.
#출력: Q줄에 걸쳐 실험의 결과 출력. i번째 줄에는 i번째 실험의 결과.

N, Q = map(int, input().split())
# 실험순서 대로 번호를 덮어씌우려고함.
board = [[0] * N for _ in range(N)]


#같은 번호 칸들이 하나의 연결 덩어리인지 봐야 해서 BFS/DFS가 필요
#시뮬레이션: 투입 -> 분리 검사 -> 이동 -> 점수 계산

from collections import deque
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def remove_split_microbes(board):
    visited = [[False] * N for _ in range(N)]

    #각 미생물 번호가 몇 덩어리인지 저장함.
    group_count = {}
    #board전체를 순회한다.
    for r in range(N):
        for c in range(N):
            #빈칸이면 검사하지 않는다.
            if board[r][c] == 0:
                continue
            #이미 BFS로 방문한 칸이면 다시 검사하지 않느다.
            if visited[r][c]:
                continue
            #여기까지 왔다는 것은 아직 방문하지 않은 미생물 칸을 발견했다는 것이다.
            #고로 실험번호로 채운다.
            microbe_id = board[r][c]
            # 이 미생물 번호에 대해 딕셔너리에 저장한다.
            if microbe_id not in group_count:
                # 처음 발견했을때 0으로 초기화한다.
                group_count[microbe_id] = 0
            #덩어리(한 무리)를 발견할때마다 값을 1로 증가시킨다.
            group_count[microbe_id] += 1

            #여기서 부터 BFS를 수행한다.
            queue = deque()
            #행과 열을 넣는다.
            queue.append((r, c))
            #방문처리를 한다.
            visited[r][c] = True
            #BFS시작
            while queue:
                #현재 행과 열을 꺼낸다.
                cur_r, cur_c = queue.popleft()
                #상하좌우를 확인한다.
                for dr, dc in dirs:
                    nr = cur_r + dr
                    nc = cur_c + dc
                    #격자 밖이면 제외한다.
                    if not (0 <= nr < N and 0<= nc < N):
                        continue
                    #이미 방문했으면 제외한다.
                    if visited[nr][nc] == True:
                        continue
                    # 같은 미생물 번호가 아니면 제외한다.
                    if board[nr][nc] != microbe_id:
                        continue
                    #같은 번호이고, 연결된 칸이면 방문 처리한다.
                    if board[nr][nc] == microbe_id and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    #둘 이상으로 나뉜 미생물 번호를 찾는다.
    remove_ids = set()
    for microbe_id in group_count:
        #해당 미생물 번호의 덩어리 개수가 2개 이상이면, 삭제 대상이다.
        # BFS를 수행하면 같은 덩어리가 연결되어있으면, 1번만 카운트할때, 2번 카운트했다는 것은
        #분리되어있다는 뜻.
        if group_count[microbe_id] >= 2:
            #리무브 아이디에 넣는다.
            remove_ids.add(microbe_id)

    #나뉜 미생물은 전부 삭제한다.
    for r in range(N):
        for c in range(N):
            if board[r][c] in remove_ids:
                board[r][c] = 0

# 새로운 배양용기로 이동시킴
# 기존 보드를 복사해서. 새 보드를 만듦..
def move_microbes(board):
    new_board = [[0] * N for _ in range(N)]
    # 이 과정은 기존 배양 용기에 미생물이 한마리도 존재하지 않을 때까지 다음 작업을 반복함.
    #현재 board에서 미생물 번호별 좌표 목록을 모은다
    microbe_cells = {}
    for r in range(N):
        for c in range(N):
            #다시 훑어보면서 정리함.
            microbe_id = board[r][c]
            # 만약 0이면 건너뛴다.
            if board[r][c] == 0:
                continue
            #만약 미생물 번호가 딕셔너리에 없다면,
            if microbe_id not in microbe_cells:
                # 그 미생물 번호가 딕셔너리에 없으면 빈 리스트로 초기화한다.
                microbe_cells[microbe_id] = []
            # 초기화, 이후, 미생물번호를 발견하면, 행, 열을 저장한다.
            microbe_cells[microbe_id].append((r, c))

    # 미생물 번호들을 영역 넓이 큰 순으로 정렬한다.
    microbe_ids = list(microbe_cells.keys())
    # 영역 넓이가 같으면 번호가 작은 순으로 정렬한다
    # 넓이 가 큰 순, 그리고 넓이가 같으면 번호가 작은순.
    microbe_ids.sort(key=lambda microbe_id: (-len(microbe_cells[microbe_id]), microbe_id))
    # 정렬된 순서대로 미생물을 하나씩 선택한다.
    for microbe_id in microbe_ids:
        # 미생물을 하나 선택한다. 해당 미생물번호의 좌표들이 모아져있다.
        cells = microbe_cells[microbe_id]
    # 선택한 미생물의 좌표 목록에서 기준점을 정한다.
        #미생물 좌표들 중 가장 위쪽 행을 base_r로 잡는다.
        base_r = min(r for r,c in cells)
        #미생물 좌표들 중 가장 왼쪽 열을 base_c로 잡는다.
        base_c = min(c for r,c in cells)
    # 기준점으로부터 각 칸의 상대 위치를 구한다. 상대좌표란 기준점에서 각 칸이 얼마나 떨어져있는지이다.
        #기존 미생물 좌표에서 모양만 뽑느다.
        shape = []
        for r, c in cells:
            shape.append((r-base_r, c -base_c))

    # 새 배양 용기에서 가능한 위치를 찾는다.
        placed = False
    # 가능한 위치는 범위 밖으로 나가지 않고, 다른 미생물과 겹치지 않는 위치다.

        for new_r in range(N): # x좌표 작은순 (바깥 반복문)
            for new_c in range(N): #y좌표 작은순 (안쪽 반복문)
                can_place = True
                positions = []
                #shape의 각 칸을 new_r, new_c 기준으로 놓아본다.
                for dr, dc in shape:
                    nr = new_r + dr
                    nc = new_c + dc
                    # 범위 밖이면 놓을 수 없다.
                    if not (0 <= nr < N and 0<= nc < N):
                        can_place = False
                        break
                    #이미 다른 미생물이 있으면 놓을 수 없다.
                    if new_board[nr][nc] != 0:
                        can_place = False
                        break
                    positions.append((nr, nc))
                #모든 칸을 놓을 수 있으면, 실제로 배치한다.
                if can_place:
                    for nr, nc in positions:
                        new_board[nr][nc] = microbe_id
                    placed = True
                    break
            if placed:
                break
# placed가 False면 어디에도 못 놓은 것이다.
# 이 경우 new_board에 쓰지 않았으므로 자동으로 사라진다.
    return new_board
#각 미생물의 넓이와 , 서로 맞닿은 미생물 쌍이 필요함.

def calculate_score(board):
    area = {}
    for r in range(N):
        for c in range(N):
            microbe_id = board[r][c]
            if microbe_id ==0:
                continue
            # 현재 미생물 칸 번호의 칸 개수를 1증가시킨다.
            # microbe_id의 값을 가져오고 없으면 0을 가져온다.
            area[microbe_id] = area.get(microbe_id, 0) + 1
    #인접한 미생물 쌍 저장
    pairs = set()
    for r in range(N):
        for c in range(N):
            #빈칸이면 지나치고
            if board[r][c] == 0:
                continue
            a = board[r][c]
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                #격자 밖이면
                if not(0 <=nr < N and 0<=nc < N):
                    continue
                #보드값이 0이면
                if board[nr][nc] ==0:
                    continue
                b = board[nr][nc]
                # 값이 같으면, 인접한 곳이 그냥 같은 한무리면 건너고
                if a == b:
                    continue

                # (1, 2)와 (2, 1)을 같은 쌍으로 처리한다.
                # sorted로 번호 순서를 통일하고, tuple로 바꿔 set에 넣는다.
                pairs.add(tuple(sorted((a, b))))
    #모든 인접 쌍의 넓이 곱을 더한다.
    score = 0

    for a, b in pairs:
        score += area[a] * area[b]
    return score

for microbe_id in range(1, Q+1):
    r1, c1, r2, c2 = map(int, input().split())
    # 1. 새 미생물 투입
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = microbe_id
            # 2. 둘 이상으로 나뉜 미생물 삭제
    remove_split_microbes(board)
    # 3. 새 배양 용기로 이동
    board = move_microbes(board)
    # 4. 실험 결과 출력
    print(calculate_score(board))