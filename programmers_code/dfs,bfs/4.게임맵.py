# 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.
# => 최단거리 문제

# 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동합니다.
# => 상하좌우 4방향 이동, 이동 비용은 모두 1

# 게임 맵을 벗어난 길은 갈 수 없습니다.
# => 범위 체크 필요

# maps는 0과 1로만 이루어져 있습니다.
# 0은 벽이 있는 자리, 1은 벽이 없는 자리입니다.
# => 1만 이동 가능

# 처음에 캐릭터는 좌측 상단 (1,1)에 있습니다.
# => 코드에서는 (0,0)에서 시작

# 상대방 진영은 우측 하단 (n,m)에 있습니다.
# => 코드에서는 (n-1, m-1)이 도착지

# 도착할 수 없을 때는 -1을 return합니다.
# => BFS 종료 후 도착 못 하면 -1
# 지나온 칸 수를 세는 문제.

# 큐 모듈 임포트
from collections import deque

def solution(maps):
    # 1. maps의 행 개수와 열 개수를 구한다.
    # n은 maps의 (세로) 길이, 행 개수
    n = len(maps)
    # m은 가로 길이, 열 개수
    m = len(maps[0])
    queue = deque()
    # n행 m열짜리 False 표를 만든다.
    visited = [[False] * m for _ in range(n)]
    # 2. 큐에 시작점을 넣는다.
    queue.append((0, 0, 1)) # row, col, distance
    visited[0][0] = True
    # 3. 상하좌우로 갈 수 있는 칸을 큐에 넣기전, 변화량을 정의
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 큐에 확인할 칸이 남아 있는 동안 계속 탐색을 반복할 것을 정의.
    while queue:
        # 큐에서 맨 앞칸을 꺼냄.
        row, col, distance = queue.popleft()
        if row == n-1 and col == m-1:
            return distance
        # 4. 현재 칸에서 상하좌우로 갈 수 있는 칸을 찾음.
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            # 4-1. 그 칸이 지도 범위에 있는지
            if 0 <= next_row < n and 0 <= next_col < m:
                # 4-2. 그 칸이 갈 수 있는 길인지 그리고 방문한 적이 없는지,
                if maps[next_row][next_col] ==1 and not visited[next_row][next_col]:
                    # 4-3. 방문처리 하기
                    visited[next_row][next_col] = True
                    # 4-4. 큐에 넣기.
                    queue.append((next_row, next_col, distance +1))

    # 상대팀 진영에 도달할 수 없을때.
    return -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# 11

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
# -1

pass