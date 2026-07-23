# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baby-whale-first-voyage/description
from collections import deque
# 1단계 : 인접 칸 검사 + 시뮬레이션
# 2단계: BFS 최단거리 목표 선택

#헤엄칠 수 있는 바다 칸의 개수
# 아기 고래 (r, c)에서 출발, 처음에 바라보는 방향  d번
# 처음에 바라보는 방향 d
# d는 1이 상, 2가 하, 3이 좌, 4가 우 -> BFS할$때는 선택칸까지의 거리가 1 줄어드는 인접한 칸 중하나로

# 0. 초기값 세팅
# board[i][j] = 격자 정보
# 0 = 바다
# 1 = 암초
# 문제 좌표가 1번부터 시작하므로 N + 1 크기로 생성
# 1번 인덱스부터 사용하려고 맞춤
# [문법 각주]
# input() = 한 줄 입력받기
# split() = 공백 기준으로 나누기
# map(int, ...) = 나눈 값을 정수로 바꾸기
# N = 격자 크기
# r, c = 시작 위치
# d = 시작 방향
N, r, c, d = map(int, input().split())
# [문법 각주]
# [[0] * (N + 1) for _ in range(N + 1)]
# = 2차원 배열 생성
# N + 1을 쓰는 이유 = 1번 행부터 N번 행까지 그대로 쓰기 위해 0번 칸을 버림
board = [[0] * (N + 1) for _ in range(N + 1)]

# [문법 각주]
# range(1, N + 1) = 1부터 N까지 반복
# row[j - 1] = 입력 row는 0번 인덱스부터 시작하므로 j에서 1을 뺌
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, N+1):
        board[i][j] = row[j-1]

# visited[i][j] = 고래 방문 여부
visited = [[False] * (N + 1) for _ in range(N + 1)]

# answer = 방문한 바다 칸 순서
answer = []

# 시작 위치 방문 처리
visited[r][c] = True
answer.append((r, c))


# 1. 방향 번호를 좌표 이동값으로 변환
# 1 = 위쪽 방향
# 2 = 아래쪽 방향
# 3 = 왼쪽 방향
# 4 = 오른쪽 방향
move = {
    1: (-1, 0),  # 행 -1
    2: (1, 0),   # 행 +1
    3: (0, -1),  # 열 -1
    4: (0, 1)    # 열 +1
}


# 2. 현재 방향 d별 검사 순서
# 순서 = 직진 → 좌회전 → 우회전 → 뒤돌기
priority = {
    1: [1, 3, 4, 2],
    2: [2, 4, 3, 1],
    3: [3, 2, 1, 4],
    4: [4, 1, 2, 3]
}

# 2. 인접한 칸에 방문가능한 바다가 없을 때
# 2-1. BFS로 목표 칸 찾기
# 가장 가까운 미방문 바다 칸 찾기
# find_target(r, c)
# = 현재 위치에서 가장 가까운 미방문 바다 찾기
def find_target(r, c):
    # dist[i][j] = 현재 위치 (r, c)에서 (i, j)까지 가는 최소 이동 횟수
    # -1 = 아직 도달 못 한 칸
    dist = [[-1] * (N+1) for _ in range(N+1)]
    # BFS 큐
    q = deque()
    # 시작 위치 넣기 .
    q.append((r, c))
    #현재 위치에서 현재 위치까지 거리는 0
    dist[r][c] = 0
    # BFS로 모든 바다 칸까지 거리 계산
    while q:
        #현재 칸 꺼내기
        cr, cc = q.popleft()
        #4개 방향 검사
        for nd in [1,2,3,4]:
            dr, dc = move[nd]
            nr = cr + dr
            nc = cc + dc
            # 격자 밖이면 제외
            if not (1 <= nr <= N and 1 <= nc <= N):
                continue
            # 암초면 제외
            if board[nr][nc] == 1:
                continue
            # 이미 거리 계산한 칸이면 제외 (dist에 이미 들어간 값이면)
            if dist[nr][nc] != -1:
                continue
            # 다음 칸 거리 기록
            dist[nr][nc] = dist[cr][cc] + 1
            # 다음 탐색 대상으로 큐에 넣기
            q.append((nr, nc))
    #목표 후보 저장
    candidates = []

    #모든 칸 검사
    for i in range(1, N+1):
        for j in range(1, N+1):
            #바다 칸이고
            #아직 방문 안했고
            #현재 위치에서 갈 수 있으면
            if board[i][j] == 0 and not visited[i][j] and dist[i][j] != -1:
                #선택 기준: 거리, 행, 열
                candidates.append((dist[i][j], i, j))
    # 갈수 있는 미방문 바다가 없으면 None
    if not candidates:
        return None
    #거리 작은 순, 행 작은 순, 열 작은순으로 정렬
    candidates.sort()
    #첫번째 후보가 목표 칸
    _, tr, tc = candidates[0]
    return (tr, tc)

def move_to_target(r, c, target):
    #목표 칸 좌표
    tr, tc= target
    # target_dist[i][j] =(i, j)에서 목표 칸까지 가는 최소 이동 횟수
    # -1 = 목표 칸까지 갈 수 없음
    target_dist = [[-1] * (N+1) for _ in range(N+1)]
    # BFS큐
    q = deque()
    #목표칸에서 BFS시작
    q.append((tr, tc))
    target_dist[tr][tc] = 0
    #목표 칸 기준 거리 표 만들기
    while q:
        cr, cc = q.popleft()

        for nd in [1,2,3,4]:
            dr, dc = move[nd]
            nr = cr + dr
            nc = cc + dc
            # 격자 밖이면 제외
            if not (1 <= nr <= N and 1 <= nc <= N):
                continue
            #암초면 제외
            if board[nr][nc] == 1:
                continue
            #이미 거리 계산한 값이면 제외
            if target_dist[nr][nc] != -1:
                continue
            #목표까지 거리기록
            target_dist[nr][nc] = target_dist[cr][cc] + 1
            q.append((nr, nc))
    #실제 이동 우선순위
    # 좌 -> 하 -> 우-> 상
    path_priority = [3,2,4,1]
    # 현재 위치가 목표 칸이 될 때까지 이동
    while (r, c) != (tr, tc):
        for nd in path_priority:
            dr, dc = move[nd]
            nr = r+dr
            nc = c+dc
            #격자 밖이면 제외
            if not (1 <= nr <= N and 1 <= nc <= N):
                continue
            #암초면 제외
            if board[nr][nc] == 1:
                continue
            #목표까지 거리가 1 줄어드는 칸이면 이동
            if target_dist[nr][nc] ==target_dist[r][c] -1:
                #현재 위치 갱신
                r, c= nr, nc
                #방향 갱신
                d = nd
                # 처음 방문한 바다 칸이면 방문 처리
                if not visited[r][c]:
                    visited[r][c] = True
                    answer.append((r, c))
                #한 칸 이동했으므로 방향 검사 종료
                break
    #도착 위치와 마지막 방향 반환
    return r, c, d
# 전체 진행
while True:

    # 1단계: 인접 탐험
    # 인접한 미방문 바다 칸으로 이동할 수 있는 동안 반복
    while True:
        # 이번 반복에서 이동했는지 기록
        moved = False

        # 현재 방향 d 기준 검사 순서를 하나씩 꺼냄
        for nd in priority[d]:

            # 방향 번호 nd를 좌표 이동값으로 변환
            dr, dc = move[nd]

            # 후보 칸 좌표 계산
            nr = r + dr
            nc = c + dc

            # 후보 칸 조건:
            # 1. 격자 안
            # 2. 바다 칸
            # 3. 미방문 칸
            if 1 <= nr <= N and 1 <= nc <= N and board[nr][nc] == 0 and not visited[nr][nc]:

                # 후보 칸 방문 처리
                visited[nr][nc] = True

                # 방문 순서 기록
                answer.append((nr, nc))

                # 현재 위치 갱신
                r, c = nr, nc

                # 현재 방향 갱신
                d = nd

                # 이동 성공 기록
                moved = True

                # 한 칸 이동했으므로 방향 검사 종료
                break

        # 네 방향 모두 갈 수 없으면 인접 탐험 종료
        if not moved:
            break

    # 2단계: 가장 가까운 미방문 바다 찾기
    target = find_target(r, c)

    # 더 갈 수 있는 미방문 바다가 없으면 전체 종료
    if target is None:
        break

    # 3단계: 목표 칸까지 이동
    r, c, d = move_to_target(r, c, target)


for r, c in answer:
    print(r, c)