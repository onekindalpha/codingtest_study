#격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수
#지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냄
# 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룸
# 지도에 적힌 숫자는 식량을 나타내고, 상하좌우로 연결되는 칸에 적힌 숫자를 모두 합한 값은
# 무인도에서 최대 며칠동안 머물 수 있는지를 나타냄
# 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return
# 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return
from collections import deque

def solution(maps):
    answer = []
    rows = len(maps)
    #일단 콜럼수는 첫행만 알아도 알 수 있느까.
    cols = len(maps[0])
    #방문표를 만듦.
    visited = [[False] * cols for _ in range(rows)]
    dirs = [
        (0, 1),  # 우
        (1, 0),  # 하
        (0, -1),  # 좌
        (-1, 0),  # 상
    ]
    # maps 전체 칸을 순회한다.
    # 행을 차례대로 꺼낸다. 0부터....
    for i in range(rows):
        ## j는 현재 행에서 열 인덱스를 의미한다.
        for j in range(cols):
            #(i, j) = maps[i][j]
            # 바다이면 BFS 시작 안 함 : BFS를 시작할 수 있는 칸인지 본다.
            if maps[i][j] == "X":
                continue
            # 이미 방문한 땅이면 BFS 시작 안 함 : BFS를 시작할 수 있는 칸인지 본다.
            if visited[i][j]:
                continue
            #여기까지 왔다는 건 새 무인도 시작점임.
            queue = deque()
            #현재 찾은 시작점인(i, j)를 넣느다.
            queue.append((i, j))
            #방문했으니까.
            visited[i][j] = True
            land = 0
            # land.sorT()
            while queue:
                #BFS중 현재 꺼낸 좌표
                x, y = queue.popleft()
                #현재 칸의 식량을 더함(중요)
                land += int(maps[x][y])
                #상하좌우로 인접한 칸을 보기
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    ## maps의 행 인덱스는 0부터 rows - 1까지만 가능하다.
                    # maps의 열 인덱스는 0부터 cols - 1까지만 가능하다.
                    # 격자 범위 밖이면 제외
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    #  현재 칸의 상하좌우 이웃칸을 큐에 넣어도 되는지 본다.
                    if maps[nx][ny] == "X":
                        continue
                    # 현재 칸의 상하좌우 이웃칸을 큐에 넣어도 되는지 본다.
                    if visited[nx][ny]:
                        continue
                    queue.append((nx, ny))
                    visited[nx][ny] = True
            # BFS가 끝나면 무인도 하나의 식량 합을 answer에 저장한다.
            answer.append(land)
    if answer == []:
        return [-1]
    answer.sort()
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))