from collections import deque

# =========================
# 상수 정의
# =========================

# 거북이가 아직 이동 중인 상태
MOVING = 0

# 거북이가 더 이상 이동하지 않는 상태
# 안식처 도착 / 화석화 모두 종료로 처리
FINISHED = -1

# =========================
# 입력 처리
# =========================

# N: 격자 크기
# M: 바다거북 수
# K: 해저 화산 수
N, M, K = map(int, input().split())

# board[r][c] = 지도 정보
# 0: 바다
# 1: 산호초
board = [list(map(int, input().split())) for _ in range(N)]

# turtles[m] = [현재 행, 현재 열, 상태, 도착 턴]
# turtles[m][0] = m번 거북이 현재 행
# turtles[m][1] = m번 거북이 현재 열
# turtles[m][2] = m번 거북이 상태
# turtles[m][3] = m번 거북이 도착 턴
#
# 처음에는 도착하지 않았으므로 도착 턴을 -1로 둔다
turtles = [[0, 0, MOVING, -1] for _ in range(M + 1)]

# turtle_map[r][c] = 해당 칸에 있는 살아있는 거북이 번호
# 0이면 거북이가 없는 칸
turtle_map = [[0] * N for _ in range(N)]

# M마리 거북이의 시작 위치 입력
for m in range(1, M + 1):
    r, c = map(int, input().split())

    # m번 거북이의 시작 위치와 상태 기록
    turtles[m] = [r, c, MOVING, -1]

    # 지도 위에 m번 거북이 위치 표시
    turtle_map[r][c] = m

# P[r][c] = 해당 칸 화산의 폭발 기준 p
# 0이면 화산이 없는 칸
P = [[0] * N for _ in range(N)]

# volcanoes = 화산 좌표 목록
# 매 턴 화산들을 돌면서 열 증가 / 폭발 처리를 하기 위해 사용
volcanoes = []

# current[r][c] = 화산 현재 열
current = [[0] * N for _ in range(N)]

# K개 화산 정보 입력
for _ in range(K):
    r, c, p = map(int, input().split())

    # 해당 위치 화산의 폭발 기준 기록
    P[r][c] = p

    # 화산 좌표 목록에 추가
    volcanoes.append((r, c))


# =========================
# 방향 정의
# =========================

# 이동 우선순위: 우, 하, 좌, 상
# BFS에서 이 순서로 넣으면 같은 거리 후보 중 우선순위가 반영됨
directions = [
    (0, 1),    # 우: 열 + 1
    (1, 0),    # 하: 행 + 1
    (0, -1),   # 좌: 열 - 1
    (-1, 0)    # 상: 행 - 1
]

# =========================
# BFS 함수
# =========================

def bfs(m):
    # m번 거북이의 현재 위치
    sr, sc = turtles[m][0], turtles[m][1]

    # visited[r][c] = BFS에서 해당 칸을 이미 확인했는지 여부
    visited = [[False] * N for _ in range(N)]

    # queue에 들어가는 값:
    # r, c = BFS가 현재 확인 중인 칸
    # first_r, first_c = 시작점에서 처음 이동한 칸
    queue = deque()

    # 시작점 넣기
    # 아직 이동한 칸이 없으므로 first도 시작점으로 둔다
    queue.append((sr, sc, sr, sc))

    # 시작점 방문 처리
    visited[sr][sc] = True

    while queue:
        # BFS에서 확인할 칸 꺼내기
        r, c, first_r, first_c = queue.popleft()

        # 안식처에 도착한 경로를 찾은 경우
        if (r, c) == (N - 1, N - 1):
            # 실제 거북이는 한 칸만 이동해야 하므로
            # 최단경로의 첫 번째 칸을 반환
            return (first_r, first_c)

        # 우, 하, 좌, 상 순서로 다음 칸 확인
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            # 격자 밖이면 이동 불가
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 이미 BFS에서 확인한 칸이면 다시 확인하지 않음
            if visited[nr][nc]:
                continue

            # 산호초 칸 또는 화석 칸이면 이동 불가
            if board[nr][nc] == 1 or board[nr][nc] == 2:
                continue

            # 다른 살아있는 거북이가 있는 칸이면 이동 불가
            # 나중에 화석도 turtle_map 또는 board에 표시하면 여기서 같이 막을 수 있음
            if turtle_map[nr][nc] != 0:
                continue

            # 여기까지 통과했으면 BFS 후보 칸으로 사용 가능
            visited[nr][nc] = True

            # 현재 칸이 시작점이면,
            # 다음 칸 (nr, nc)가 최단경로의 첫 번째 이동 칸
            if (r, c) == (sr, sc):
                queue.append((nr, nc, nr, nc))

            # 시작점 이후의 칸이면,
            # 처음 이동한 칸 first_r, first_c를 계속 들고 간다
            else:
                queue.append((nr, nc, first_r, first_c))

    # 안식처까지 갈 수 있는 경로가 없으면 제자리
    return (sr, sc)

#=======
# 2단계 화산 내부 마그마 압력 증가
#=======
def increase_heat():
    for r, c in volcanoes:
        current[r][c] += 10

#======
# 3단계 이번 턴 분출 열기 기록
# =====

def process_eruption():
    # 이번 턴 칸마다 닿은 열기
    heat_map = [[0] * N for _ in range(N)]

    #이번턴에 폭발한 화산 목록
    exploded = []

    # 이미 분출한 화산 확인용
    exploded_set = set()

    # 앞으로 열기를 퍼뜨릴 화산 대기줄
    queue = deque()
    # 1. 자기 압력만으로 분출하는 화산 찾기
    for r, c in volcanoes:
        if current[r][c] >= P[r][c]:
            exploded.append((r, c))
            exploded_set.add((r, c))
            queue.append((r, c))
            # 분출한 화산 자기 칸에도 열기가 있다고 표시
            heat_map[r][c] += P[r][c]
    # 2. 큐가 빌 때까지 연쇄 분출 처리
    while queue:
        r, c = queue.popleft()

        # 이 화산이 뿜는 열기의 시작값
        start_heat = P[r][c]
        #우, 하, 좌, 상 4방향 전파
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            heat = start_heat // 2

            while 0 <= nr < N and 0 <= nc < N and heat >0:
                #산호초면 열기 전파 중단
                if board[nr][nc] == 1:
                    break
                #이 칸에 열기 누적
                heat_map[nr][nc] += heat

                # 이 칸이 화산이고, 아직 이번 턴 분출하지 않았다면
                if P[nr][nc] > 0 and (nr, nc) not in exploded_set:
                    #이 시점의 heat_mpa[nr][nc]는
                    #아직 분출하지 않은 화산 입장에서는 외부에서 들어온 열기
                    if current[nr][nc] + heat_map[nr][nc] >= P[nr][nc]:
                        exploded.append((nr, nc))
                        exploded_set.add((nr, nc))
                        queue.append((nr, nc))

                        #새로 분출한 화산 자기 칸에도 열기 표시
                        heat_map[nr][nc] += P[nr][nc]
                # 다음 칸으로 이동
                nr += dr
                nc += dc
                heat //=2
    return heat_map, exploded

# ========
# 3단계 바다거북
#=========
def fossilize_turtles(heat_map):
    # 모든 거북이를 확인
    for m in range(1, M + 1):
        #이미 종료된 거북이는 확인하지 않음
        if turtles[m][2] != MOVING:
            continue
        #m번 거북이 현재 위치
        r, c = turtles[m][0], turtles[m][1]

        #이번 턴 누적 열기가 20 이상이면 위기
        if heat_map[r][c] >= 20:
            #거북이 종료 처리
            turtles[m][2] = FINISHED
            #도착하지 못했으므로 결과 시간은 -1
            turtles[m][3] = -1
            #살아있는 거북이 위치표에서 제거
            turtle_map[r][c] = 0
            #해당 칸을 화석으로 표시
            board[r][c] = 2
#========
# 4단계 환경 초기화
#========
def reset_erupted_volcanoes(exploded):
    #이번 턴 분출한 화산들의 현재 마그마 입력을 0으로 초기화
    for r, c in exploded:
        current[r][c] = 0

# =========================
# 턴 시뮬레이션
# =========================

# 최대 100턴 진행
for turn in range(1, 101):

    # =========================
    # 1단계: 거북이 이동
    # =========================

    # 1번 거북이부터 M번 거북이까지 순서대로 이동
    for m in range(1, M + 1):

        # 이미 종료된 거북이는 이동하지 않음
        if turtles[m][2] != MOVING:
            continue

        # 현재 위치
        r, c = turtles[m][0], turtles[m][1]

        # BFS로 이번 턴에 이동할 한 칸 계산
        nr, nc = bfs(m)

        # 기존 위치에서 거북이 제거
        turtle_map[r][c] = 0

        # m번 거북이 위치 갱신
        turtles[m][0] = nr
        turtles[m][1] = nc

        # 안식처에 도착한 경우
        if (nr, nc) == (N - 1, N - 1):

            # m번 거북이 종료 처리
            turtles[m][2] = FINISHED

            # m번 거북이 도착 턴 기록
            turtles[m][3] = turn

            # 안식처 도착 거북이는 지도에서 제외
            turtle_map[nr][nc] = 0

        # 아직 안식처가 아니면
        else:
            # 새 위치에 m번 거북이 표시
            turtle_map[nr][nc] = m

    # =========================
    # 2단계: 화산 열 증가
    # =========================
    increase_heat()

    # =========================
    # 3단계: 분출 / 열기 전파 / 연쇄 반응
    # =========================
    heat_map, exploded = process_eruption()

    # =========================
    # 3단계: 바다거북 위기
    # =========================
    fossilize_turtles(heat_map)

    # =========================
    # 4단계: 분출한 화산 초기화
    # =========================
    reset_erupted_volcanoes(exploded)

# =========================
# 출력
# =========================
# turtles[m][3] = m번 거북이 도착 턴
# 1번 거북이부터 M번 거북이까지 도착 턴 출력
# 도착하지 못한 거북이는 -1 출력
for m in range(1, M + 1):
    print(turtles[m][3])