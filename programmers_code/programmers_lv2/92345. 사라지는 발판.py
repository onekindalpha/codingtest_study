# 양 캐릭터가 몇 번 움직이게 될지.
# 캐릭터를 올려놓는 곳은 항상 발판이 있고, 발판 있는 곳으로만 이동할 수 있음.
# 캐릭터가 이동하는 순간. 그 발판이 사라짐.
# 상하좌우.
# 움직일 차례인데 상하좌우 모두 발판 없고, 보드 밖이라 이동  못하면 해당 차례에 패배
# 두 캐릭터가 같은 발판일때, 상대 캐릭터가 다른 발판으로 이동해서 자신이 서있는 발판이 사라지면 패배함
# a가 항상 먼저 시작함. 이길 수 있는 플레이어는 최대한 빨리 승리하도록, 질 수 밖에 없는 플레이어는 최대한 오래 버티도록 - 많이 움직이는 것
# board = 게임 보드의 초기 상태를 나타내는 2차원 정수 배열
# aloc = 플레이어 a의 캐릭터 초기 위치를 나타내는 정수 배열
# bloc = 플레이어 b의 캐릭터 초기 위치를 나타내는 정수 배열
# 양 플레이어가 최적의 플레이를 했을대, 두 캐릭터가 움직인 횟수의 합을 return

def solution(board, aloc, bloc):
    row = len(board)
    col = len(board[0])

    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def can_go(r, c):
        if r < 0 or r >= row or c < 0 or c >= col:
            return False

        if board[r][c] == 0:
            return False

        return True

    def play(cur_r, cur_c, other_r, other_c):
        # 현재 사람이 서 있는 발판이 이미 사라졌으면 패배
        if board[cur_r][cur_c] == 0:
            return False, 0

        can_current_win = False

        # 내가 이길 수 있는 경우들 중 가장 짧은 이동 횟수
        min_win_count = float("inf")

        # 내가 질 수밖에 없는 경우들 중 가장 긴 이동 횟수
        max_lose_count = 0

        for dr, dc in direction:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if not can_go(next_r, next_c):
                continue

            # 현재 사람이 이동하므로 현재 발판 제거
            board[cur_r][cur_c] = 0

            # 다음 차례는 상대
            other_can_win, move_count = play(
                other_r,
                other_c,
                next_r,
                next_c
            )

            # 다른 경우도 봐야 하므로 복구
            board[cur_r][cur_c] = 1

            total_move_count = move_count + 1

            # 상대가 지는 상태면 현재 사람은 이길 수 있음
            if not other_can_win:
                can_current_win = True
                min_win_count = min(min_win_count, total_move_count)
            else:
                max_lose_count = max(max_lose_count, total_move_count)

        # 여기부터는 for문 밖이어야 함
        if can_current_win:
            return True, min_win_count

        return False, max_lose_count

    # 여기도 play 함수 밖이어야 함
    can_a_win, answer = play(aloc[0], aloc[1], bloc[0], bloc[1])
    return answer


print(solution(
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [1, 0],
    [1, 2]
))
# 5

print(solution(
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [1, 0],
    [1, 2]
))
# 4

print(solution(
    [[1, 1, 1, 1, 1]],
    [0, 0],
    [0, 4]
))
# 4

print(solution(
    [[1]],
    [0, 0],
    [0, 0]
))
# 0