# key sentences
# 만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.
# 가장 짧은 거리를 return -> 최단 거리 문제
# 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다. x3
# 2차원, 최대 50, rectangle = [x1, y1, x2, y2] -> 좌측 하단 (x1, y1), 우측 상단 (x2, y2)
# 캐릭터는 이 다각형의 둘레(굵은 선)을 따라서 이동합니다.
# 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.
# 캐릭터 위치 ( , ), 아이템 위치 ( , ), 최단 이동 거리 구하기

# 모듈 임포트
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 102x102 크기의 빈 지도판 만들고 모든 칸을 0으로 채워봄.
    board = [[0] * 102 for _ in range(102)]

    # 1. 직사각형들을 보드에 표시해봄.
    # 직사각형을 살펴보며 테두리인지, 내부 면인지 구분해봄.
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 +1):
                if x == x1 or x == x2 or y == y1 or y == y2:
                    if board[y][x] != 2:
                        board[y][x] = 1
                else:
                    board[y][x] = 2

    # 직사각형을 구분했으면, BFS를 실행할 준비를 해봄.
    # 큐(x좌표, y좌표, 지금까지 이동거리)랑 방문 배열 만들어봄.

    # 2. 캐릭터와 아이템 좌표도 2배함.
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    #3. BFS 준비
    # 큐 비어있음
    queue = deque()
    # 102x102크기로, 처음에는 전부 False인게 정상
    visited = [[False] * 102 for _ in range(102)]

    # 캐릭터 시작위치에서 출발함. 시작위치를 넣음. 이동거리는 0.
    queue.append((characterX, characterY, 0))
    # 방문한 곳은 True가 됨.
    visited[characterY][characterX] = True
    # 상하좌우 변화량 배열 만들기
    # x의 변화량, y의 변화량
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 4. BFS 반복문
    # 4-1. 큐에서 현재 위치 꺼내봄. 큐는 계속 반복함.
    while queue:
        x, y, distance = queue.popleft()
        # 4-2. 꺼내서 아이템 위치면 거리를 반환함. 끝난다는 뜻.
        if x == itemX and y == itemY:
            return distance // 2
        # 4-3. 아니면 상하좌우를 확인함. 4번 반복함.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 4-4. 갈 수 있으면 큐에 넣음. 새 좌표가 테두리 길이고 방문하지 않은 곳이면 방문처리. 한칸씩 이동.
            if board[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, distance +1))

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],
                1,3,7,8
))  #17

print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],
                9,7,6,1
)) #11

print(solution([[1,1,5,7]],
                1,1,4,7
)) #9
print(solution([[2,1,7,5],[6,4,10,10]],
                3,1,7,10
)) #15

print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],
                1,4,6,3
)) #10

pass