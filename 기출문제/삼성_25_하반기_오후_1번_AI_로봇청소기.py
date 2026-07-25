# 함수호출===============
from collections import deque
# ====================
# =====
# 입력
# =====

# 격자의 크기, 로봇 청소기의 개수, 테스트 횟수
# 첫줄: N, K, L, 공백으로 구분되어
N, K, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

robots = []
for i in range(K):
    r,c = map(int, input().split())
    robots.append([r-1,c-1])

# =========================
# 격자 해석
# =========================
# board[r][c] = 해당 칸의 상태값 p
#
# p == -1 : 물건이 있는 칸
# p == 0  : 먼지가 없는 빈 칸
# p > 0   : 먼지가 있는 칸
#           문제 조건상 1 ~ 100

# =========================
# 이동 가능 여부
# =========================
# p == -1 : 물건 칸이므로 이동 불가
# p != -1 : 물건이 아니므로 이동 가능 후보
# 이동 불가 조건:
# board[nr][nc] == -1

# =========================
# 로봇 초기 위치
# =========================
# 각 로봇은 초기 위치 r, c를 가진다.
# → robots에 저장한다.
#
# 초기 위치에는 먼지가 없음이 보장된다.
# → 시작 칸은 board[r][c] == 0으로 생각해도 됨
# → 시작하자마자 먼지를 청소하는 처리는 필요 없음

# 테스트
# 1. 청소기 이동 : 이동거리가 가장 가까운 오염된 격자
# 청소기는 순서대로, 이동거리가 최단인, 먼지가 있는 격자로 이동
# -1인 보드로는 이동 불가
# 이동거리는 상하좌우로, 인접한 격자, 한 칸 씩 이동, 최소 이동 횟수 -> 이동 비용은 같다?
# 가까운 격자 여러개시, 행 번호가 가장 작은 격자, 행 번호가 같을 시, 열번호 작은 격자
from collections import deque

# 청소기 이동 후보를 만듦.
def bfs(start, robot_idx):
    directions = [
        (0, 1),  # 우
        (0, -1),  # 좌
        (-1, 0),  # 상
        (1, 0),  # 하
    ]
    # 다른 로봇 위치를 막기 위한 집합 # =====해당부분 추가함. 예제2번 틀리고.
    blocked_robots = set()
    for i in range(K):
        if i == robot_idx:
            continue
        blocked_robots.add(tuple(robots[i]))

    #큐에 (시작행, 시작열, 현재까지 이동횟수 0)을 넣는다.
    queue = deque()
    queue.append((start[0], start[1], 0))
    # 방문 배열을 만든다.
    visited = [[False] * N for _ in range(N)]
    # 시작 위치를 방문 처리한다.
    sr, sc = start
    visited[sr][sc] = True
    #먼지 후보 목록 = 빈 리스트
    candidates = []
    #가장 가까운 거리 = 아직 없음
    shortest_distance = None
    #큐가 빌 때까지 반복:
    while queue:
        #현재 위치 r, c, dist를 꺼낸다.
        r, c, dist = queue.popleft()
        #만약 이미 찾은 가장 가까운 거리보다 dist가 크면
        if shortest_distance is not None and shortest_distance < dist:
            #더 볼 필요 없음
            break
        #만약 현재 칸에 먼지가 있으면,
        if board[r][c] >0:
            #먼지 후보 목록에 (r, c)를 넣는다.
            candidates.append((r, c))
            #가장 가까운 거리 = dist
            shortest_distance = dist
            #이 칸에서 더 확장하지 않는다.
            #break를 하면 먼지 하나 찾고 끝나니까, 같은 거리 먼지 후보 다 모으게
            continue
        #내 방향을 확인한다.
        for dr, dc in directions:
            #다음 칸 nr, nc를 만든다.
            nr = r + dr
            nc = c + dc

            #격자 밖이면 제외
            if nr <0 or nr >= N or nc <0 or nc >= N:
                continue
            #이미 방문했으면 제외
            if visited[nr][nc] == True:
                continue
            #물건 칸이면 제외
            if board[nr][nc] == -1:
                continue
            #로봇이 있는 칸이면 이동 불가
            if (nr, nc) in blocked_robots:
                continue
            #방문 처리한다.
            visited[nr][nc] = True
            #큐에 (nr, nc, dist+1)을 넣는다.
            queue.append((nr, nc, dist + 1))

    #먼지 후보가 없으면:
    if not candidates:
        #갈 수 있는 먼지 없음
        return None
    #먼지 후보가 있으면:

    #행 번호 작은 순, 열 번호 작은 순으로 정렬
    candidates.sort()
    #첫번째 후보를 선택
    return candidates[0]

# =========================
# 청소 방향 선택 규칙
# =========================
# 청소기는 바라보고 있는 방향을 기준으로 청소한다.
# → 가능한 바라보는 방향 후보 4개를 본다.
# → 동점 우선순위가 오른쪽, 아래쪽, 왼쪽, 위쪽이므로
# → 방향 후보 순서도 [우, 하, 좌, 상]으로 둔다.
#
# 본인이 위치한 격자, 자신의 왼쪽 격자, 앞쪽 격자, 오른쪽 격자를 청소할 수 있다.
# → 어떤 방향을 바라본다고 가정했을 때
# → 현재 칸 + 왼쪽 칸 + 앞쪽 칸 + 오른쪽 칸 = 총 4칸을 만든다.
#
# 청소할 수 있는 4가지 격자에서 청소할 수 있는 먼지량이 가장 큰 방향에서 청소를 시작한다.
# → 각 방향마다 4칸의 청소 가능 먼지량 합을 계산한다.
# → 합이 가장 큰 방향을 선택한다.
#
# 격자마다 청소할 수 있는 최대 먼지량은 20이다.
# → 한 칸에서 실제 청소 가능한 양 = min(board[nr][nc], 20)
#
# 합이 같은 방향이 여러 개면 오른쪽, 아래쪽, 왼쪽, 위쪽 우선순위로 선택한다.
# → 방향 후보를 [우, 하, 좌, 상] 순서로 검사한다.
# → total > best_total 일 때만 갱신한다.
# → total == best_total이면 먼저 나온 방향을 그대로 둔다.

# 2. 청소 : 먼지량이 가장 큰 우선순위로 청소
def clean(start):
    # 현재 위치 r, c에서 방향 후보 4개를 본다 = 고 가정한다.
    r, c = start
    # 방향 순서 = 오른쪽, 아래쪽, 왼쪽, 위쪽
    dirs = [
        (0, 1), #0: 우
        (1, 0), #1: 하
        (0, -1), #2: 좌
        (-1, 0), #3: 상
    ]

    # 시계방향으로 이동하면 dir_idx +1, 반시계방향으로 이동하면 dir_idx -1
    best_sum = -1
    best_zone = None
    # 각 방향 dir에 대해:
    for dirs_idx in range(4):
        # 내가 보는 방향
        front = dirs[dirs_idx]
        # 시계방향. 한바퀴 돌았을 경우도 생각해서 4로 나눔.
        right = dirs[(dirs_idx + 1) % 4]
        # 반시계방향. 한바퀴 돌았을 경우도 생각해서 4로 나눔.
        left = dirs[(dirs_idx - 1) % 4]
        #이번 방향에서 청소할 수 있는 먼지량 합계를 구할 것이다.
        total = 0
        # 청소 가능한 4칸을 구한다.
        available_zone = [
            (r, c), #현재칸
            (r + left[0], c + left[1]), #왼쪽칸
            (r + front[0], c + front[1]), #앞쪽칸
            (r + right[0], c + right[1]), #오른쪽칸
        ]
        #각 칸에 대해:
        for nr, nc in available_zone:
            # 격자 밖이면 제외
            if nr <0 or nr >= N or nc <0 or nc >= N:
                continue
            # 물건이면 제외
            if board[nr][nc] == -1:
                continue
            # 먼지가 있으면 min(먼지량, 20)을 total에 더함.
            if board[nr][nc] > 0:
                total += min(board[nr][nc], 20)
        # 이번 방향에서 청소할 수 있는 먼지량 합계를 구할 것이다.
        #total이 best_sum보다 크면:
        if total > best_sum:
            best_sum = total
            best_zone = available_zone
        #total이 같으면 이미 방향 순서를 우, 하, 좌, 상으로 들고 있으므로 그대로 둠

    #best_zone이 정해지면 그 방향 기준 4칸을 실제로 청소한다
    for nr, nc in best_zone:
        #격자 밖이면 제외한다.
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        #물건이면 제외한다.
        if board[nr][nc] == -1:
            continue
        #먼지가 있으면
        if board[nr][nc] > 0:
            clean_amount = min(board[nr][nc], 20)
            board[nr][nc] -= clean_amount

# 3. 먼지 축적
# =========================
# 먼지 축적
# =========================
# 먼지가 있는 모든 격자에 동시에 5씩 추가된다.
#
# 먼지가 있는 칸:
# board[r][c] > 0
#
# 빈 칸:
# board[r][c] == 0 → 추가하지 않음
#
# 물건 칸:
# board[r][c] == -1 → 추가하지 않음

def add_dust():
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                board[r][c] += 5
# 일단 함수만 만듦.

# 4. 먼지 확산
def spread_dust():
    dirs = [
                    (0, 1),  # 우
                    (1, 0),  # 하
                    (0, -1),  # 좌
                    (-1, 0),  # 상
                ]
#먼지 확산량 계산을 위해 기존 격자를 복사한다.
    new_board = [row[:] for row in board]
    #모든 격자를 하나씩 확인한다.
    for r in range(N):
        for c in range(N):
        # 물건이 있거나 먼지가 있으면 제외한다.
            if board[r][c] ==-1 or board[r][c] >0:
                continue
            dust_sum = 0
            # 현재 칸이 깨끗한 격자이면
            #주변 4방향 격자의 먼지량 합을 구한다.

            #주변 4방향을 확인해서 주변 4방향 좌표를 알 수 있다.
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                #격자 밖이면 제외
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                #먼지가 있으면
                if board[nr][nc] >0:
                    dust_sum += board[nr][nc]

            #현재 깨끗한 격자 칸에 먼지 확산
            new_board[r][c] +=dust_sum // 10
    return new_board

# 호출 board = spread_dust()
# 5. 출력
# 전체 공간의 총 먼지량을 출력함.
# 먼지가 없는 곳이면 0을 출력함
# 각 테스트가 끝날 때마다 공간에 있는 총 먼지의 합을 줄마다 출력함.
# 위 테스트 과정을 L번 반복함.
for l in range(L):
    #1. 모든 로봇을 순서대로 이동시킨다.
    for i in range(K):
        # i번 로봇의 현재 위치에서 갈 먼지 칸 찾기
        target = bfs(robots[i], i)
        #갈 수 있는 먼지 칸이 있으면 그 칸으로 이동
        if target is not None:
            #i번 로봇의 현재 위치를 그 먼지 칸으로 바꾸기
            robots[i] = [target[0], target[1]]
    #2. 모든 로봇을 순서대로 청소시킨다.
    for i in range(K):
        start = robots[i]
        clean(start)
    #3. 먼지를 축적한다.
    add_dust()
    #4. 먼지를 확산한다.
    board = spread_dust()
    #4. 전체 먼지량을 출력한다.
    total_dust = 0
    # 격자를 하나씩 살펴보면서
    for r in range(N):
        for c in range(N):
            #먼지가 있으면
            if board[r][c] > 0:
                #총 먼지량 합에 그 격자의 먼지를 더하고
                total_dust += board[r][c]
    print(total_dust)

# 시뮬레이션이라서 현재 상태(robots)를 계속 갱신
