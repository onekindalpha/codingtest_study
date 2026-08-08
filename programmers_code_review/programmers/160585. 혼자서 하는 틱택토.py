# 1. 혼자서 하는 틱택토 : 실수를 했는지 아닌지를 보면 되겠다가고 읽다가, 밑에 설명에서 "실수를 했을 가능성이 있는가"를 묻는게 아닌 이 게임판이 규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황인가를 묻는 문제라는 것에 유의하라고 되어있었는데, 그 둘의 차이가 궁금했다. 어떤 차이이지? 일단 규칙대로 했으면 1이고 아니면 0인 듯 하다. 규칙대로 했으면 나올 수 있는 상황인지.  일단 한 사람이 게임을 하고.
# 2. N = len(board)
# board2 = ["O.X", ".O.", "..X"]
# board1 = ["OOO", "...", "XXX"]
# board3 = ["...", ".X.", "..."]
# board4 = ["...", "...", "..."]
# board = [
#     "OXO",
#     "XXO",
#     "OXX"
# ]

# 누가 이겼는지에 (선공 또는 후공) 따라 게임 규칙을 잘 지키고 있는지 알 수 있어서
def is_win(board, mark):
    N = len(board)
    # 4. board = 보드가 그려진다.
    # 6. 규칙2) 가로., 세로, 대각선으로 3개 같은 표시가 만들어지면 같은 표시를 만든 사람이 승리하고 게임이 종료된다.
    for row in board:
        # 가로 세개가 같은 표시일때 (같은 것들이 빈칸이 아닌지 검사)
        if row[0] == mark and row[1] == mark and row[2] == mark:
            return True
# 세로 세개가 같은 표시일때.
    for col in range(N):
        if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark:
            return True
# 대각선3개가 같은 표시일때
    if board[0][0] == mark and board[1][1] == mark and board[2][2] ==mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] ==mark:
        return True
    return False

def count_check(board):
    N = len(board)
    x_count = 0
    o_count = 0
    blank_count = 0
    for row in board:
        x_count +=row.count("X")
        o_count +=row.count("O")
    return x_count, o_count


    # 선공은 O, 후공은 X임. 따라서, 1) 선공이 이겼을때 X보다 1 많은건 불가 2) 후공이 이겼을때 O랑 개수 같지 않은 건 불가

        #무승부라서 게임을 진행할 수 없으면 게임을 종료해야 함.
    # 5. 규치1) 선공이 O, 후공이 X이다.
    # 선공
    # start = "O"
    # #후공
    # next = "X"

    # 8. 규칙4) 혼자 선공과 후공을 둘 다 맡는다.

    # 9. 규칙5) 틱택토 게임을 시작한 후 "O"와 "X"를 혼자서 번갈아 가면서 표시를 하면서 진행핱ㄴ다.

    # 10. 규칙6) 한 게임이 종료되면 다시 3x3 빈칸을 그린 뒤 다시 게임을 반복한다.ㅏ

    # 11. 규칙7) 틱택토 수십 판을 했더니, 머쓱이는 게임 도중에 규칙을 어기는 실수를 했을 수도 없다. 예를 들어, 1)"O"을 표시할 차례인데 "X"를 표시하거나,

    # "X"를 표시할 차례인데 , :"O"을 표시한다. 2) 선공과 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다.
def is_valid(board):
    x_count, o_count = count_check(board)
    o_win = is_win(board, "O")
    x_win = is_win(board, "X")
    # 1. X가 O보다 많으면 안 됨
    if x_count > o_count:
        return 0

    # 2. O가 X보다 2개 이상 많으면 안 됨
    if o_count > x_count + 1:
        return 0

    # 3. O와 X가 둘 다 이기면 안 됨
    if o_win and x_win:
        return 0

    # 4. O가 이겼다면 O가 마지막 수여야 함
    if o_win and o_count != x_count + 1:
        return 0

    # 5. X가 이겼다면 X가 마지막 수여야 함
    if x_win and o_count != x_count:
        return 0

    return 1

    # 12. 규칙8) 딱 어느 시점의 게임판을 봤을때 실제로 틱택토 규칙을 지켜서 진행했을 때, 나올 수 있는 상황인지를 판단하고, 문제가 없으면 게임을 이어서 한다.
def solution(board):
    return is_valid(board)
    # 13. 규칙9) 어느 순간의 게임판 정보를 담은 문자열 배열 board가 매개벼눗로 주어지고, 이 게임판이 규칙을 지켜서 나올 수 있는 게임 상황이면 1을 아니라면 0을 리턴한다.
