up = [0, 1]
down = [0, -1]
left = [-1, 0]
right = [1, 0]


def solution(keyinput, board):
    #1. board의 가로 크기와 세로 크기
    board_width = board[0]
    board_height = board[1]

    map_x = board[0] // 2
    map_y = board[1] // 2

    x = 0
    y = 0

    for i in keyinput:

        if i =="left" and x > -map_x:
            x -= 1
        if i =="right" and x < map_x:
            x += 1
        if i == "up" and y < map_y:
            y += 1
        if i == "down" and y > -map_y:
            y -= 1

    return [x, y]

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
# [2, 1]

print(solution(["down", "down", "down", "down", "down"], [7, 9]))
# [0, -4]