# 시작위치에서 출발한 뒤 목표 위치에 정확하게 멈추기 위해 최소 몇 번의 이동이 필요한지
# 상, 하, 좌, 우 중 한 방향으로 장애물이나 게임판 가장자리에 부딪힐 때까지 미끄러져 움직이는 것을 한번의 이동
# "." 빈 공간, "R" 로봇의 처음 위치, "D"는 장애물의 위치, "G"는 목표지점

# 목표지점에 도달할 수 없다면 -1 을 return
# 빈 공간, 장애물, 로봇의 처음 위치, 목표 지점
# R(로봇의 처음 위치)와 G(목표 지점)은 한번씩 등장함

from collections import deque

def solution(board):
    answer = 0
    #행의 수
    rows = len(board)
    #열의 수
    cols = len(board[0])
    dirs = [
        (-1, 0),  # 상
        (1, 0),  # 하
        (0, -1),  # 좌
        (0, 1),  # 우
    ]
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "R":
                start_r = row
                start_c = col
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((start_r, start_c, 0))
    visited[start_r][start_c] = True
    while queue:
        #count는 현재 좌표까지 오기 위해 미끄러진 횟수
        cur_r, cur_c, count = queue.popleft()
        #목표지점에 도달하면 카운트를 반환
        #목표지점에 왔다는거 자체가 D가 옆에있었다는 의미임.
        if board[cur_r][cur_c] == "G":
            return count
        for dr, dc in dirs:
            #현재 위치를 복사해서, 그 방향으로 미끄러질 임시 위치를 만듦.
            move_r = cur_r
            move_c = cur_c
            while True:
                # 하지만 while문 안에서 계속 더하므로 한 방향으로 쭉 이동하게 된다.
                next_r = move_r + dr
                next_c = move_c + dc

                if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                    break

                if board[next_r][next_c] == "D":
                    break
                # 다음 칸으로 이동 가능하므로 임시 위치를 갱신한다.
                move_r = next_r
                move_c = next_c
            if visited[move_r][move_c]:
                continue
            visited[move_r][move_c] = True
            # 실제로 멈춘칸이다.
            queue.append((move_r, move_c, count + 1))

# BFS를 다 돌았는데 G에 멈춘 적이 없으면 도달 불가능
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))