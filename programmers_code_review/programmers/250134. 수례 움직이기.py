# 빨간 수레와 파란 수레는 각각 자기 시작 칸에서 자기 도착 칸까지 이동해야 한다.
# 각 턴마다 모든 수레를 상하좌우 인접한 칸 중 하나로 움직여야 한다.
# 수레는 벽이나 격자 밖으로 움직일 수 없다.
# 수레는 자신이 방문했던 칸으로 다시 갈 수 없다.
# 도착 칸에 도착한 수레는 더 이상 움직이지 않는다.
# 두 수레가 동시에 같은 칸으로 움직이면 안 된다.
# 두 수레가 서로 자리를 바꾸면서 움직이면 안 된다.
# 퍼즐을 푸는 데 필요한 턴의 최솟값을 return한다.
# 풀 수 없으면 0을 return한다.

def solution(maze):
    # 줄 개수, 위 아래 방향 개수
    row_count = len(maze)
    # 한 줄 안의 칸 개수, 왼쪽 오른쪽 방향 개수
    col_count = len(maze[0])

    red_start = None
    blue_start = None
    red_target = None
    blue_target = None

    for row in range(row_count):
        for col in range(col_count):
            if maze[row][col] == 1:
                red_start = (row, col)
            elif maze[row][col] == 2:
                blue_start = (row, col)
            elif maze[row][col] == 3:
                red_target = (row, col)
            elif maze[row][col] == 4:
                blue_target = (row, col)

    # 상하좌우
    directions = [(-1, 0), # row -=1 (위)
                  (1, 0), # row += 1 (아래)
                  (0, -1), # col -=1 (왼쪽)
                  (0, 1)] # col +=1 (오른쪽)

    # 수레의 다음 칸 후보 만들기
    def get_next_positions(position, target, visited):
        # 이미 도착했으면 움직이지 않는다. 그래서 현재 위치 그대로 후보로 준다.
        if position == target:
            return [position]

        row, col = position
        next_positions = []
        # 상ㅎ;ㅏ좌우를 하나씩 꺼낸다.
        for row_move, col_move in directions:
            next_row = row + row_move
            next_col = col + col_move
            # 이제 못 가는 칸을 걸러낸다. (1) 격자 밖인지, (2) 벽인지, (3) 방문했던 칸인지)
            # 줄 번호가 이상하고 위 아래 밖으로 나간 경우
            if next_row <0 or next_row >= row_count:
                continue
            # 칸 번호가 이상하고 왼쪽/오른쪽 밖으로 나간 경우
            if next_col<0 or next_col >= col_count:
                continue
            if maze[next_row][next_col] == 5:
                continue
            if (next_row, next_col) in visited:
                continue
            # 여기까지 안걸리면 갈 수 있는 칸
            next_positions.append((next_row, next_col))
        return next_positions

        # 지금까지의 최소 턴 수
    answer = float("inf")

        # 빨강과 파랑의 다음 후보 목록
    def dfs(red_position, blue_position, red_visited, blue_visited, turn_count):
            # 바깥 solution 안에 있는 answer를 고침.
        nonlocal answer
            # 둘 다 도착했으면 끝
        if red_position == red_target and blue_position == blue_target:
            answer = min(answer, turn_count)
            return

        red_next_positions = get_next_positions(red_position, red_target, red_visited)
        blue_next_positions = get_next_positions(blue_position, blue_target, blue_visited)

        for red_next in red_next_positions:
            for blue_next in blue_next_positions:
                    # 같은 칸에 있으면 버린다
                if red_next == blue_next:
                    continue
                    # 서로 자리 바꾸면 버림
                if red_next == blue_position and blue_next == red_position:
                    continue
                    # 이제 가능한 조합이면 방문 기록을 업데이트한다.
                next_red_visited = set(red_visited)
                next_blue_visited = set(blue_visited)
                    # 아직 도착 전이면 방문기록 추가
                if red_position != red_target:
                    next_red_visited.add(red_next)
                if blue_position != blue_target:
                    next_blue_visited.add(blue_next)

                dfs(
                    red_next,
                    blue_next,
                    next_red_visited,
                    next_blue_visited,
                    turn_count +1
                )
    # 여기서 실제 탐색 시작
    dfs(red_start, blue_start, {red_start}, {blue_start}, 0)
    # 끝까지 못 찾았으면 0
    if answer == float("inf"):
        return 0
    # 찾았으면 최소 턴 수
    return answer

# =========================
# 테스트 코드
# =========================

def run_test(maze, expected):
    result = solution(maze)
    print("maze:")
    for row in maze:
        print(row)
    print("result  :", result)
    print("expected:", expected)
    print("PASS" if result == expected else "FAIL")
    print("-" * 30)


# 테스트 1
# 빨강: (0,0) -> (2,1)
# 파랑: (2,0) -> (0,1)
# 둘 다 3턴이면 도착 가능
run_test(
    [
        [1, 4],
        [0, 0],
        [2, 3]
    ],
    3
)


# 테스트 2
# 서로 방해 안 하고 바로 도착하는 경우
# 빨강: 오른쪽, 오른쪽
# 파랑: 오른쪽, 오른쪽
run_test(
    [
        [1, 0, 3],
        [5, 5, 0],
        [2, 0, 4]
    ],
    2
)


# 테스트 3
# 빨강이 벽 때문에 도착할 수 없음
run_test(
    [
        [1, 5, 3],
        [5, 5, 5],
        [2, 0, 4]
    ],
    0
)


# 테스트 4
# 이미 도착한 수레는 멈춰 있어야 하는 경우
# 빨강은 1턴에 도착
# 파랑은 2턴에 도착
run_test(
    [
        [1, 3],
        [2, 0],
        [0, 4]
    ],
    2
)


# 테스트 5
# 같은 칸으로 동시에 가면 안 되는지 확인하는 용도
run_test(
    [
        [1, 0, 4],
        [0, 0, 0],
        [2, 0, 3]
    ],
    4
)