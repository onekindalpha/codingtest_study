def solution(m, n, board):
    # m = 행 개수
    # n = 열 개수
    # board = 문자열 배열

    # 문자열 행을 문자 리스트로 바꾼다.
    # board[r][c] 형태로 값을 바꾸기 위해 필요하다.
    board = [list(row) for row in board]

    # 지운 블록 개수
    answer = 0

    # 2x2 삭제가 없을 때까지 반복한다.
    while True:
        # 한 턴에서 지울 좌표 저장
        # set은 같은 좌표를 한 번만 저장한다.
        remove = set()

        # 2x2의 왼쪽 위 칸 후보를 돈다.
        # r+1을 보므로 마지막 행은 제외한다.
        for r in range(m - 1):
            # c+1을 보므로 마지막 열은 제외한다.
            for c in range(n - 1):

                # 빈칸은 2x2 검사 대상이 아니다.
                if board[r][c] == " ":
                    continue

                # 현재 칸, 오른쪽, 아래, 오른쪽 아래가 같은지 확인한다.
                if board[r][c] == board[r][c + 1] == board[r + 1][c] == board[r + 1][c + 1]:
                    # 2x2에 포함된 네 칸을 삭제 후보에 넣는다.
                    remove.add((r, c))
                    remove.add((r, c + 1))
                    remove.add((r + 1, c))
                    remove.add((r + 1, c + 1))

        # 지울 좌표가 없으면 반복 종료
        if not remove:
            break

        # set에 저장된 좌표 수만큼 삭제 개수 증가
        answer += len(remove)

        # 삭제 후보 좌표를 빈칸으로 바꾼다.
        for r, c in remove:
            board[r][c] = " "

        # 블록 떨어뜨리기
        # 모든 열을 처리한다.
        for c in range(n):
            # 현재 열에서 살아 있는 블록 저장
            blocks = []

            # 위에서 아래로 보면서 빈칸이 아닌 블록만 모은다.
            for r in range(m):
                if board[r][c] != " ":
                    # 위에 있던 블록 -> 아래에 있던 블록 순으로 모음
                    blocks.append(board[r][c])

            # 아래에서 위로 채운다.
            # range(m - 1, -1, -1)은 m-1부터 0까지 돈다.
            # -1은 포함되지 않는다.
            for r in range(m - 1, -1, -1):
                # 남은 블록이 있으면 아래 칸부터 채운다.
                if blocks:
                    #pop()은 리스트의 마지막 값을 꺼냄.
                    #.pop()는 뒤에서 꺼냄.
                    board[r][c] = blocks.pop()
                # 남은 블록이 없으면 빈칸으로 채운다.
                else:
                    board[r][c] = " "

    return answer

# #blocks.pop()    -> 마지막 원소 꺼냄
# blocks.pop(0)   -> 첫 번째 원소 꺼냄
# blocks.pop(i)   -> i번 인덱스 원소 꺼냄