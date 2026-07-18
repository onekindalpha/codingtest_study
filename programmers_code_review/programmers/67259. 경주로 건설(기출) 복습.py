# 건설비용은 직선도로 x 개수에 코너 곱하기 개수다
# 2차원 배열 board는 도면의 상태(0 비어 있음, 1은 벽)을 나타냄
# 경주로 건설하는데 필요한 최소 비용
# n은 3에서 5이다
# 우측 하단은 n-1, n-1
# board 배열의 원소인 0은 도로 연결 가능, 1은 도로 연결 불가능
# board는 항상 경주로를 건설할 수 있는 형태로 주어짐
# 출발점과 도착점 원소의 값은 항상 0
# 어떻게 해야 경주로 건설 비용을 최소화하는지
# 최단비용에 음수간선 없으니까 다익스트라인듯.

import heapq

def solution(board):
    n = len(board)

    # 방향: 위, 아래, 왼쪽, 오른쪽
    directions = [
        (-1, 0),  # 0: 위
        (1, 0),   # 1: 아래
        (0, -1),  # 2: 왼쪽
        (0, 1)    # 3: 오른쪽
    ]

    INF = float('inf')

    # dist[y][x][dir]
    # y, x 칸에 dir 방향으로 도착했을 때의 최소 비용
    dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    # heap에는 후보를 넣는다: 비용, y, x, 이전 방향
    heap = []

    # 비용 0, 위치 (0, 0), 아직 이전 방향 없음
    heapq.heappush(heap, (0, 0, 0, -1))

    while heap:
        # 현재까지 후보들 중 비용이 가장 작은 후보를 꺼낸다
        cost, y, x, prev_dir = heapq.heappop(heap)

        # 현재 위치가 도착점이면 최소 비용 반환
        if y == n - 1 and x == n - 1:
            return cost

        # 4방향 확인
        for new_dir in range(4):
            dy, dx = directions[new_dir]

            ny = y + dy
            nx = x + dx

            # 범위 밖이면 무시
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            # 벽이면 무시
            if board[ny][nx] == 1:
                continue

            # 비용 계산
            if prev_dir == -1:
                new_cost = cost + 100
            elif prev_dir == new_dir:
                new_cost = cost + 100
            else:
                new_cost = cost + 600

            # 더 싼 비용으로 도착할 수 있으면 갱신
            if new_cost < dist[ny][nx][new_dir]:
                dist[ny][nx][new_dir] = new_cost
                heapq.heappush(heap, (new_cost, ny, nx, new_dir))


print(solution([
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,1],
    [0,0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0]
]))
# 예상 출력: 3800

print(solution([
    [0,0,1,0],
    [0,0,0,0],
    [0,1,0,1],
    [1,0,0,0]
]))
# 예상 출력: 2100

print(solution([
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,1,0,0,0],
    [1,0,0,1,0,1],
    [0,1,0,0,0,1],
    [0,0,0,0,0,0]
]))
# 예상 출력: 3200