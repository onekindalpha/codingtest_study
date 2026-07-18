# 열쇠는 회전과 이동이 가능하다.
# key는 0도, 90도, 180도, 270도 네 방향을 모두 확인해야 한다.

# 자물쇠 영역을 벗어난 key 부분은 영향을 주지 않는다.
# 그래서 key가 lock 밖으로 삐져나가는 위치도 확인해야 한다.

# 자물쇠 영역 안에서는 key의 돌기와 lock의 홈이 정확히 맞아야 한다.
# lock 영역의 모든 값이 최종적으로 1이 되어야 열린다.

# key의 돌기와 lock의 돌기가 만나면 안 된다.
# lock 영역에서 key + lock 값이 2가 되면 실패다.

# 모든 위치와 모든 회전을 시도해야 하므로 구현 + 완전탐색 문제다.


# 열쇠는 회전과 이동이 가능하다.
# key는 0도, 90도, 180도, 270도 네 방향을 모두 확인해야 한다.

# 자물쇠 영역을 벗어난 key 부분은 영향을 주지 않는다.
# 그래서 key가 lock 밖으로 삐져나가는 위치도 확인해야 한다.

# 자물쇠 영역 안에서는 key의 돌기와 lock의 홈이 정확히 맞아야 한다.
# lock 영역의 모든 값이 최종적으로 1이 되어야 열린다.

# key의 돌기와 lock의 돌기가 만나면 안 된다.
# lock 영역에서 key + lock 값이 2가 되면 실패다.

# 모든 위치와 모든 회전을 시도해야 하므로 구현 + 완전탐색 문제다.


def solution(key, lock):
    n = len(lock)
    m = len(key)

    board_size = n * 3
    for _ in range(4):
        #큰 보드 만들기
        board=[[0] * board_size for _ in range(board_size)]
        # lock을 가운데에 넣기
        for y in range(n):
            for x in range(n):
                board[y + n][x + n] = lock[y][x]
        #key를 가능한 모든 위치에 올려보기
        for by in range(0, board_size - m +1):
            for bx in range(0, board_size - m +1):

                # key더하기
                for y in range(m):
                    for x in range(m):
                        board[by + y][bx + x] += key[y][x]
                # board[y][x]는 key를 올려본 결과값이 됨.
                # 가운데 lock이 전부 1이면 성공
                if check(board, n):
                    return True

                # key 다시 빼기
                for y in range(m):
                    for x in range(m):
                        board[by + y][bx + x] -= key[y][x]
        # 다음 회전을 위해 key올리기
        key = rotate(key)

    return False


def check(board, n):
    for y in range(n, 2 * n):
        for x in range(n, 2 * n):
            if board[y][x] != 1:
                return False
    return True


def rotate(key):
    m = len(key)
    rotated = [[0] * m for _ in range(m)]

    for y in range(m):
        for x in range(m):
            rotated[x][m - 1 - y] = key[y][x]

    return rotated


def run_tests():
    tests = [
        # 프로그래머스 예제
        (
            [[0, 0, 0],
             [1, 0, 0],
             [0, 1, 1]],
            [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]],
            True
        ),

        # 이미 자물쇠가 다 1인 경우
        (
            [[1]],
            [[1, 1],
             [1, 1]],
            True
        ),

        # key 1개가 lock 홈 1개를 채우는 경우
        (
            [[1]],
            [[0]],
            True
        ),

        # key가 홈을 못 채우는 경우
        (
            [[0]],
            [[0]],
            False
        ),

        # 돌기끼리 부딪히는 경우
        (
            [[1]],
            [[1]],
            True
        ),

        # 회전해야만 열리는 경우
        (
            [[1, 0],
             [1, 0]],
            [[1, 1],
             [0, 1]],
            True
        ),

        # 위치 이동이 필요한 경우
        (
            [[1, 0],
             [0, 0]],
            [[1, 1],
             [1, 0]],
            True
        ),

        # 홈이 여러 개인데 key 돌기가 부족한 경우
        (
            [[1, 0],
             [0, 0]],
            [[0, 0],
             [0, 1]],
            False
        ),
    ]

    for i, (key, lock, expected) in enumerate(tests, 1):
        result = solution(key, lock)
        if result == expected:
            print(f"TEST {i}: PASS")
        else:
            print(f"TEST {i}: FAIL")
            print("expected:", expected)
            print("result  :", result)
            print("key     :", key)
            print("lock    :", lock)


run_tests()