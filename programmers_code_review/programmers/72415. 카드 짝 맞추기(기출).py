# 남은 카드를 모두 제거하는 데 필요한 키 조작 횟수의 최솟ㅂㅅ
# 방향 키 + enter 도 1회, ctrl+ 방향키 도 1회
# 이것도 아마 bfs가 아닐까 싶은데
# 빈칸은 카드 제거된 칸
# 그림이 그려진 칸은
# 특이점:
# 이동중에
# 앞면이 보이는 카드가 1장이면 두번째 카드를 뒤집을 때까지 앞면을 유지함.
# 2개가 될때, 앞면이 보이는 그림이 그려진 카드의 그림이 같으면 화면에서 사라짐.
# 그림이 다르면 두 카드 모두 뒷면이 보이도록 뒤집힘.

# 1. 카드 위치를 모은다.
# 2. Ctrl 이동 함수를 만든다.
# 3. BFS로 현재 위치 → 목표 위치 최소 이동 횟수를 구한다.
# 4. DFS로 어떤 카드부터 제거할지 전부 시도한다.
# 5. 같은 카드 2장 중 어느 쪽을 먼저 뒤집을지도 전부 시도한다.
# 6. 최솟값을 반환한다.

from collections import deque, defaultdict
from itertools import permutations

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def ctrl_move(board, row, col, dr, dc):
    #계산할때는 하나씩
    current_row = row
    current_col = col

    while True:
        next_row = current_row + dr
        next_col = current_col + dc

        if not (0 <= next_row < 4 and 0 <= next_col < 4):
            #좌표로 한번에
            return (current_row, current_col)
        #일단 한칸 이동한다.
        current_row = next_row
        current_col = next_col

        #이동한 칸에 카드가 있으면 거기서 멈춘다.
        if board[current_row][current_col] != 0:
            return (current_row, current_col)

# 현재 위치에서 목표 위치까지 몇 번 이동해야 하는지 구하는 함수.
def bfs(board, start, target):
    start_row, start_col = start
    target_row, target_col = target
    q = deque()
    visited = [[False] * 4 for _ in range(4)]
    q.append((start_row, start_col, 0))
    visited[start_row][start_col] = True
    # 먼저 들어온 위치부터 처리.
    while q:
        current_row, current_col, count = q.popleft()
        #목표 위치에 도착했으면 이동 횟수 반환
        if (current_row, current_col) == (target_row, target_col):
            return count

        for dr, dc in DIRS:
            #1. 일반 방향키 이동
            next_row = current_row + dr
            next_col = current_col + dc

            if 0 <= next_row < 4 and 0 <= next_col < 4:
                if not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col, count + 1))
            #2. ctrl이동
            ctrl_row, ctrl_col = ctrl_move(board, current_row, current_col, dr, dc)

            if not visited[ctrl_row][ctrl_col]:
                visited[ctrl_row][ctrl_col] = True
                q.append((ctrl_row, ctrl_col, count + 1))

def solution(board, r, c):
    # 1. 카드 번호별 위치를 모은다.
    # 처음보는 카드 번호가 나오면 자동으로 빈 리스트 []를 만들도록 함.
    card_positions = defaultdict(list)

    start = (r, c)

    for row in range(4):
        for col in range(4):
            card_number = board[row][col]

            if card_number != 0:
                card_positions[card_number].append((row, col))

    # 최솟값을 구하는 문제는 무한대부터 시작한느 것 같긴 함.
    answer = float("inf")

    # 2. 가능한 카드 제거 순서를 전부 만든다.
    # ex. 1번 쌍 -> 2번 쌍 -> 3번 쌍
    # ex. 1번 쌍 제거: 현재 위치 -> 1번 카드 A -> 1번 카드 B
    for order in permutations(card_positions.keys()):
        #이번 순서만 테스트할 보드를 만든다.
        #카드를 제거하는 테스트를 해야 하니까. 그럼.
        copied_board = [row[:] for row in board]

        # 커서를 처음 위치로 돌린다.
        current = start
        # 키 조작 횟수
        total = 0
        # order에 적힌 카드 번호를 하나씩 제거한다.
        for card_number in order:
            pos1, pos2 = card_positions[card_number]
            cost1 = bfs(copied_board, current, pos1) + bfs(copied_board, pos1, pos2) + 2
            cost2 = bfs(copied_board, current, pos2) + bfs(copied_board, pos2, pos1) + 2

            if cost1 <= cost2:
                total += cost1
                current = pos2
            else:
                total += cost2
                current = pos1

                # 여기
            row1, col1 = pos1
            row2, col2 = pos2

            copied_board[row1][col1] = 0
            copied_board[row2][col2] = 0
        # order 하나가 끝났으면 answer 갱신
        answer = min(answer, total)
    return answer
# 테스트 1: 프로그래머스 예제
board1 = [
    [1, 0, 0, 3],
    [2, 0, 0, 0],
    [0, 0, 0, 2],
    [3, 0, 1, 0]
]

print(solution(board1, 1, 0))  # 기대값: 14


# 테스트 2: 프로그래머스 예제
board2 = [
    [3, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [2, 0, 0, 3]
]

print(solution(board2, 0, 1))  # 기대값: 16