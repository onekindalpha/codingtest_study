# 1와 0로 채워진 표(board)가 있습니다.
# 표(board)는 2차원 배열로 주어집니다.
# 표(board)의 행(row)의 크기 : 1,000 이하의 자연수
# 표(board)의 열(column)의 크기 : 1,000 이하의 자연수
# DP / 2차원 배열 문제

def solution(board):
    # 줄의 길이
    row_count =  len(board)
    # 한 줄 안에 있는 칸의 개수
    col_count = len(board[0])
    # dp를 사용하는 이유는, 가장 큰 정사각형 한 변의 길이를 구하려고 함
    dp = [[0] * col_count for _ in range(row_count)]
    # 가장 큰 정사각형 한변의 길이
    max_side = 0
    # 현재 칸이 1일때만 본다.
    # 현재 칸을 "오른쪽 아래 꼭짓점"으로 하는 정사각형의 한변 길이는
    # 왼쪽/ 위/왼쪽 위가 만들어줄 수 있는 정사각형 크기 중
    # 가장 작은 값 + 현재 칸 1개임.
    for row in range(row_count):
        for col in range(col_count):
            # 만약에 한 변의 길이가 1인데 첫번째 줄이거나, 첫번째 칸이면, 그 칸은 한 변 길이 1자리 정사각형까지만 만들 수 있다.
            if board[row][col] == 1:
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    # 바로 왼쪽
                    dp[row][col] = min(
                        dp[row][col-1],
                    # 바로 왼쪽 윗
                        dp[row-1][col-1],
                    # 바로 위
                        dp[row-1][col]
                    ) +1

            max_side = max(max_side, dp[row][col])
    return max_side * max_side

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# 9

print(solution([[0,0,1,1],[1,1,1,1]]))
# 4