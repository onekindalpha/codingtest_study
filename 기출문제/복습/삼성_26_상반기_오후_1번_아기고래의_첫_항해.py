#바다는 N×N 크기의 격자로 표현됩니다. 격자의 각 칸은 헤엄칠 수 있는 바다(0)이거나, 지나갈 수 없는 암초(1)입니다. 격자에서 i행 j열의 칸을 (i,j)로 표현합니다.
#아기 고래는 위치 (r,c)에서 출발하며, 처음에 바라보는 방향은 d입니다. 방향은 1이 상, 2가 하, 3이 좌, 4가 우를 의미합니
# 목표: 가능한 모든 바다 탐험
# 헤엄칠 수 있는 모든 바다 방문 시 종료
# 아기고래가 방문하는 바다 칸의 위치를 방문 순서대로 출력.
# 시작위치도 출력에 포함
# 처음 시작 위치는 바다임. .
# =========================
# 입력
# =========================
from collections import deque
N, r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 문제 좌표는 1부터 시작
# 파이썬 인덱스는 0부터 시작
r -= 1
c -= 1
# =========================
# 방향
# =========================
direction_map = {
    1: (-1, 0),  # 상
    2: (1, 0),   # 하
    3: (0, -1),  # 좌
    4: (0, 1),   # 우
}

# 현재 방향을 기준으로
# 정면 → 왼쪽 → 오른쪽 → 반대
priority = {
    1: [1, 3, 4, 2],
    2: [2, 4, 3, 1],
    3: [3, 2, 1, 4],
    4: [4, 1, 2, 3],
}

# 2단계에서 실제로 이동할 때의 우선순위
# 좌 → 하 → 우 → 상
path_priority = [3, 2, 4, 1]

# =========================
# 방문 상태
# =========================
visited = [[False] * N for _ in range(N)]

# 시작 위치 방문 처리
visited[r][c] = True

# 실제로 지나간 칸을 순서대로 저장
# 시작 위치도 포함
visit_order = [(r, c)]

# =========================
# 2단계 첫 번째 BFS
# 가장 가까운 미방문 바다 찾기
# =========================
def find_nearest_target(start_r, start_c):
    queue = deque([(start_r, start_c)])
    #dist[i][j]
    #현재 위치에서 (i, j)까지의 최단거리
    dist = [[-1] * N for _ in range(N)]
    dist[start_r][start_c] = 0

    while queue:
        cr, cc = queue.popleft()

        #거리만 구하는 BFS이므로
        #방향 확인 순서는 목적지 선택에 영향을 주지 않음.
        for next_d in range(1, 5):
            dr, dc = direction_map[next_d]
            nr =cr +dr
            nc =cc +dc

            if not(0 <= nr < N and 0 <= nc < N):
                continue
            #암호는 통과 불가
            if board[nr][nc] ==1:
                continue
            #이번 BFS에서 이미 확인한 칸
            if dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[cr][cc] + 1
            queue.append((nr, nc))

    candidates = []
    #아직 방문하지 않은 바다를 후보로 수집
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not visited[i][j]:
                #현재 위치에서 도달할 수 있는 칸만 후보
                if dist[i][j] != -1:
                    #거리 -> 행 -> 열 순서로 저장
                    candidates.append((dist[i][j], i, j))
    if not candidates:
        return None
    #거리 최소
    #거리가 같으면 행 최소
    #행 도 같으면 열 최소
    candidates.sort()
    _, target_r, target_c = candidates[0]
    return target_r, target_c

# =========================
# 2단계 두 번째 BFS
# 각 칸에서 목적지까지의 거리 계산
# =========================
def make_distance_from_target(target_r, target_c):
    queue = deque([(target_r, target_c)])
    #dist_to_target[i][j]
    #(i, j)에서 목적지까지의 최단거리
    dist_to_target = [[-1] * N for _ in range(N)]
    dist_to_target[target_r][target_c] = 0
    while queue:
        cr, cc = queue.popleft()

        for next_d in range(1, 5):
            dr, dc = direction_map[next_d]
            nr =cr +dr
            nc =cc +dc

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if board[nr][nc] == 1:
                continue
            if dist_to_target[nr][nc] != -1:
                continue
            dist_to_target[nr][nc] = dist_to_target[cr][cc] + 1
            queue.append((nr, nc))
    return dist_to_target
# =========================
# 전체 탐험
# =========================
while True:
    # =====================
    # 1단계
    # 인접한 미방문 바다 확인
    # =====================
    moved = False
    #현재 바라보는 방향 기준
    #정면 -> 왼쪽 -> 오른쪽 -> 반대
    for next_d in priority[d]:
        dr, dc = direction_map[next_d]
        nr = r +dr
        nc = c +dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if board[nr][nc] == 1:
            continue
        if visited[nr][nc]:
            continue
        #실제 이동
        r = nr
        c = nc
        #이동한 방향으로 갱신
        d = next_d
        #처음 방문한 칸
        visited[r][c] = True
        #실제 이동 우ㅟ치 기록
        visit_order.append((r, c))
        moved = True
        break
    #1단계에서 이동했다면
    # 새로운 현재 위치에서 다시 1단계 실행
    if moved:
        continue
    # =====================
    # 2단계
    # 가장 가까운 미방문 바다 선택
    # =====================
    target = find_nearest_target(r, c)
    #더 이상 도달 가능한 미방문 바다가 없음
    if target is None:
        break
    target_r, target_c = target
    #목적지에서 각 칸까지의 거리
    dist_to_target = make_distance_from_target(
        target_r,
        target_c
    )
    # =====================
    # 선택한 목적지까지 실제 이동
    # =====================
    while (r, c) != (target_r, target_c):
        path_moved = False
        #좌0->하->우0>상
        for next_d in path_priority:
            dr, dc = direction_map[next_d]
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if board[nr][nc] == 1:
                continue
            #목적지까지의 거리가 1 줄어드는 칸
            if (
                dist_to_target[nr][nc]
                == dist_to_target[r][c]-1
            ):
                r = nr
                c = nc
                #방금 이동한 방향으로 갱신
                #마지막 이동이 끝나면 마지막 방향이 남음
                d = next_d
                # 실제로 한 칸 이동했음
                path_moved = True
                #처음 방문한 경우에만 방문 처fl                # 처음 방문한 칸만 기록
                if not visited[r][c]:
                    visited[r][c] = True
                    visit_order.append((r, c))

                break
        if not path_moved:
            break
    # =========================
    # 출력
    # =========================
for vr, vc in visit_order:
    print(vr +1, vc+1)
# 선택한 칸까지 최단 거리로 이동함.
# 매 이동마다 선택한 칸 까지의 거리가 1 줄어드는 인접한 칸 중 하나로 이동하며
# 그러한 칸이 여러개라면 좌, 하, 우, 상 순서의 우선순위로 선택함
# 도착후 바라보는 방향은 마지막 이동 방향으로 갱신됨.
# 헤엄칠 수 있는 모든 바다를 방문하면 종료되고, 아기 고래가 방문하는 바다 칸의 위치를
# order = []
# 방문순서대로 출력해줘야 함. 시작 위치도 출력에 포함함.