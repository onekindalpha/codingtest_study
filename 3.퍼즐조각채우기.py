# 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓으려 합니다. -> game board는 0, 테이블은 1
# 조각은 한 번에 하나씩 채워 넣습니다.
# 조각을 회전시킬 수 있습니다.
# 조각을 뒤집을 수는 없습니다.
# 게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다. -> 빈칸이 남으면 안됨.
# 퍼즐 조각이 놓일 빈칸은 1x1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
# 퍼즐 조각은 1x1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
# 규칙에 맞게 최대한 많은 퍼즐 조각을 게임 보드에 채워 넣을 경우, 총 몇 칸을 채울 수 있는지 return

# 모듈 임포트
from collections import deque

# 붙어있는 칸들을 하나의 덩어리로 모으는 용도로서 bfs를 사용함.
def solution(game_board, table):
    n = len(game_board)

    # find_shapes 함수 만들기
    def find_shapes(board, target):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        # 배열 방향성 만들기
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        # 2차원 보드 전체를 훑기
        for y in range(n):
            for x in range(n):
        # 이 칸이 내가 찾는 숫자이고, 아직 방문하지 않은 칸이면, 새 덩어리 찾기를 시작한다.
                if board[y][x] == target and not visited[y][x]:
                    # 대기줄을 만든다.
                    queue = deque()
                    # 큐의 시작점을 만든다. 확인할 칸을 줄 맨 뒤에 넣는다.
                    queue.append((x, y))
                    visited[y][x] = True
                    # 덩어리의 좌표를 만들리스트
                    shape = []
                    # queue 반복문 만들기
                    # 큐에 확인할 칸이 남아 있는 동안 계속 반복한다.
                    while queue:
                        # 큐에서 맨 앞 칸을 꺼낸다. 그 칸의 x좌표를 cx에 넣고, 그 칸의 y좌표를 cy에 넣는다.
                        # 줄 맨 앞에 있는 칸을 꺼낸다.
                        cx, cy = queue.popleft()
                        # 칮고 있던 구멍/퍼즐 조각의 좌표 모음에 넣는다.
                        shape.append((cx, cy))
                        # 현재 칸 주변을 봄. 주변칸들의 좌표를 만듦.
                        for i in range(4):
                            nx = cx + dx[i]
                            ny = cy + dy[i]
                            if 0<= nx < n and 0 <= ny < n :
                                if board[ny][nx] == target and not visited[ny][nx]:
                                # target이 0이면 0인칸만 모으고, target이 1이면 1인칸만 모음.
                                    visited[ny][nx] = True
                                    queue.append((nx, ny))
                    shapes.append(shape)

        return shapes

    def normalize(shape):
        # shape 모음 중에 가장 작은 x와 y
        min_x = min(x for x, y in shape)
        min_y = min(y for x,y in shape)

        normalized = sorted((x - min_x, y - min_y) for x,y in shape)
        return normalized

    def rotate(shape):
        rotated = []
        for x, y in shape:
            rotated.append((-y, x))
        # 회전후 정규화를 함.
        return normalize(rotated)

    empty_spaces = find_shapes(game_board, 0)
    puzzle_pieces = find_shapes(table, 1)
    # 찾아낸 구멍들과 퍼즐 조각들도 모두 정규화한다.
    empty_spaces = [normalize(shape) for shape in empty_spaces]
    puzzle_pieces = [normalize(shape) for shape in puzzle_pieces]

    answer = 0
    used = [False] * len(puzzle_pieces)

    # 구멍 하나씩 확인한다.
    for empty in empty_spaces:
        # 처음에는 매칭이 없음.
        matched = False

        # 퍼즐 조각들을 하나씩 확인한다.
        for i in range(len(puzzle_pieces)):
            # 만약 사용했으면 건너뛴다.
            if used[i]:
                continue
            # 이번에 구멍과 비교할 퍼즐이다.
            piece = puzzle_pieces[i]

            # 퍼즐을 최대 4번(상, 하, 좌, 우) 회전해보며 비교한다.
            for _ in range(4):
                # 퍼즐 모양이랑 구멍 모양이랑 똑같은지
                if piece == empty:
                    # 구멍을 채웠으니, 정답에 칸 수를 하나 더함.
                    answer += len(empty)
                    # 사용 처리함.
                    used[i] = True
                    # 이 구멍은 퍼즐을 찾았다고 표시함.
                    matched = True
                    # 회전 비교는 이제 그만.
                    break
                # 안 맞으면 회전함. 그리고 다시 퍼즐 모양이랑 구멍 모양이랑 똑같은지 확인함.
                piece = rotate(piece)
            # 퍼즐 목록 보는 반복문을 멈춤. 다음 구멍으로 넘어간다.
            if matched:
                break

    return answer

print(solution(
    [[1,1,0,0,1,0],
     [0,0,1,0,1,0],
     [0,1,1,0,0,1],
     [1,1,0,1,1,1],
     [1,0,0,0,1,0],
     [0,1,1,1,0,0]],
    [[1,0,0,1,1,0],
     [1,0,1,0,1,0],
     [0,1,1,0,1,1],
     [0,0,1,0,0,0],
     [1,1,0,1,1,0],
     [0,1,0,0,0,0]]
))  # 14

print(solution(
    [[0,0,0],
     [1,1,0],
     [1,1,1]],
    [[1,1,1],
     [1,0,0],
     [0,0,0]]
))  # 0