# 9 x 9 스도쿠 보드를 다 채워 완성된 스도쿠 보드를 반환하는 solution()함수를 작성하세요.
# 빈칸은 0으로 주어집니ㅏㄷ.
# 가로줄 세로줄에는 1부터 9까지의 숫자가 한번씩 나타나야합니다.
# 9x9 보드를 채울 9개의 작은 박스(3x3)에도 1부터 9까지의 숫자가 한 번씩 나타나야 합니ㅏㄷ.
# 스도쿠의 조건에 맞다면 맞는 해라고 생각하시면 됩니다. -> 백트리킹을 떠올리게 합니다. (빈칸에 숫자를 넣어본다, 조건에 맞는지 확인한다, 맞으면 계속 간다, 안 맞으면 다른 숫자를 넣어본다. )

def solution(board):
    def find_empty(board):
        # index 0~8
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    def is_valid(board, row, col, num):
        # 같은 행 검사
        if num in board[row]:
            return False

        # 같은 열 검사
        for r in range(9):
            if board[r][col] == num:
                return False

        # 같은 3x3 박스 검사
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def solve(board):
        # board에서 0인 칸 하나 찾기
        empty = find_empty(board)

        # 빈칸이 없다면 스도쿠 완성
        if empty is None:
            return True

        # 빈칸이 있다면 위치 꺼내기
        row, col = empty

        # 그 빈칸에 1부터 9까지 넣어보기
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                # 유효한 숫자라면 일단 넣어본다
                board[row][col] = num

                # num을 넣은 상태로 끝까지 풀어본다
                if solve(board):
                    return True

                # 끝까지 안 풀리면 다시 빈칸으로 되돌린다
                board[row][col] = 0

        # 1부터 9까지 다 넣어봤는데 안 되면 실패
        return False

    solve(board)
    return board


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

result = solution(board)

for row in result:
    print(row)