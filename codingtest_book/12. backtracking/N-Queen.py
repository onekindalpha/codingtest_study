# n은 12이하의 자연수. 가로 세로 n인 정사각형. n개의 퀸이 서로를 공격할 숭 ㅓㅂㅅ도록 배치함.

# n은 12 이하의 자연수.
# 가로, 세로가 n인 정사각형에 n개의 퀸을 서로 공격할 수 없도록 배치하는 방법의 수를 구한다.

def solution(n):
    answer = 0
    queens = []

    # row행 col열에 퀸을 놓아도 되는지 검사하는 함수
    def is_safe(row, col):
        for prev_row, prev_col in enumerate(queens):
            # 같은 열에 이미 퀸이 있으면 안 됨
            if prev_col == col:
                return False

            # 같은 대각선에 이미 퀸이 있으면 안 됨
            if abs(row - prev_row) == abs(col - prev_col):
                return False

        return True

    # row번째 행에 퀸을 놓는 함수
    def dfs(row):
        nonlocal answer

        # n개 행에 모두 퀸을 놓았다면, 가능한 방법 하나를 찾은 것
        if row == n:
            answer += 1
            return

        # 현재 row에서 0열부터 n-1열까지 시도
        for col in range(n):
            if is_safe(row, col):
                queens.append(col)   # 현재 row에 col열 퀸을 놓음
                dfs(row + 1)         # 다음 행으로 이동
                queens.pop()         # 돌아오면 방금 놓은 퀸을 취소

    dfs(0)
    return answer


print(solution(4))  # 2