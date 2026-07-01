# 거쳐간 숫자의 합이 가장 큰 경우
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능
# 삼각형의 정보가 담긴 배열 triangle
# 거쳐간 숫자의 최댓값 return
# 삼각형의 높이는 1 이상 500 이하
# 삼각형을 이루고 있는 숫자는 0 이사 9,999 이하의 정수

def solution(triangle):
    dp = []

    dp.append([triangle[0][0]])

    for row in range(1, len(triangle)):
        current_row = []
        for col in range(len(triangle[row])):
            if col == 0:
                max_sum = dp[row-1][col] + triangle[row][col]

            elif col == row:
                max_sum = dp[row-1][col-1] + triangle[row][col]
            else:
                max_sum = max(dp[row-1][col-1], dp[row-1][col]) + triangle[row][col]
            current_row.append(max_sum)

        dp.append(current_row)
    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# 30