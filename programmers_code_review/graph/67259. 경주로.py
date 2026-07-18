# 경주로 부지 nxn , 경주로 0 or 1, 도착점 n-1, n-1
# 상하좌우 1칸씩. 상하 또는 좌우 - 직선 도로 100원 . 직각 - 코너. 500원
# 경주로 건설 최소 비용 계산
# 직선 도로 6개 x 100 + 코너 4개 x 500 = 2600원
# 직선 도로 4개 x 100 + 코너 1개 x 500 = 900원
# board 2차원 배열. 2차원 행렬 (0, 1). 3이상 25이하.
# 출발점과 도착점 칸 원소 값 0

import heapq

def solution(board):
    n = len(board)
    # if not (3 <= n <= 25):
    #     return None
    INF = float('inf')
    # 최저가표 ex. costs[row][col] = [오른쪽 방향으로 들어온 최소 비용, 왼쪽 방향으로 들어온 최소 비용, 위 방향으로 들어온 최소 비용, 아래 방향으로 들어온 최소 비용]
    costs = [[[INF] *4  for _ in range(n)] for _ in range(n)]
    # 출발점
    costs[0][0] = [0, 0, 0, 0]
    #
    # # 방향별 최소 비용
    # visited = [[False] * n for _ in range(n)]
    # 현재 칸에서 움직일 수 있는 방법 목록
    directions = [
        (0, 1), # 오른쪽
        (0, -1), # 왼쪽
        (-1, 0), # 위
        (1, 0), # 아래
    ]
    pq = []
    # 우선순위 큐 시작점. (현재까지 비용, x좌표, y좌표, 이전방향)
    heapq.heappush(pq, (0, 0, 0, -1))
    # 우선순위 큐 안에 아직 탐색할 후보가 남아있으면 계속 반복한다.
    while pq:
        # 아직 가볼 후보가 남아 있으면, 그중 비용이 가장 싼 후보를 하나 꺼낸다.
        cost, row, col, prev_dir = heapq.heappop(pq)
        # 그 후보의 현재 위치와 비용을 확인한다.
        # prev_dir은 코너 비용 계산하려고 필요함.
        # 아래 두줄은 지워도 됨.
        if row == n -1 and col == n -1:
            return cost
        # 현재 칸에서 오른쪽, 왼쪽, 위, 아래로 한 칸씩 가본다.
        for new_dir, (dr, dc) in enumerate(directions):
            next_row = row + dr
            next_col = col + dc

            # 방향 후보를 만들어서, board안 범위인지 확인해야 함.
            if next_row < 0 or next_row >=n or next_col <0 or next_col >=n:
                continue
            # 벽이면 못감
            if board[next_row][next_col] ==1:
                continue
            if prev_dir == -1 or prev_dir == new_dir:
                next_cost = cost + 100
            else:
                next_cost = cost + 600
            # 아래와 같이 짜면 처음 가는 길이면 INF 대신 최소 비용을 저장하게 됨. 이미 가본 길이면 더 싼 경우에만 저장하게 됨. 비싸면 버리게 됨.
            if next_cost < costs[next_row][next_col][new_dir]:
                costs[next_row][next_col][new_dir] = next_cost
                # 그 위치를 다음 탐색 후보에 넣는다.
                heapq.heappush(pq, (next_cost, next_row, next_col, new_dir))
    return min(costs[n - 1][n - 1])


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# 900
#
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# 3800
#
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# 2100
#
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
# 3200