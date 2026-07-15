# 2 x 1 크기의 로봇
# 0과 1로 이루어진 n x n 크기의 지도에서 (n, n) 위치까지 이동
# 0은 빈칸. 1은 벽.
# 벽이 있는 칸 또는 지도 박으로는 이동 불가.
# (1, 1), (1,2)에 놓여져 있음. 항상 0으로 주어짐.
# 90도 회전가능하고, 1초 걸림.
# 로봇이 차지하는 두 칸 중 어느 한칸이라도 (N, N) 위치에 도착하면 됨.
# 로봇이 (n, n) 위치까지 이동하는데 필요한 최소 시간 return
# 목적지에 항상 도달할 수 있음.

# 특이점: 축이 되는 칸으로부터 대각선 방향에 벽이 있으면,90도 회전을 못함.
from collections import deque

def solution(board):
    # board는 주어져있음.
    n = len(board)
    # 바깥을 벽으로 감싼 board 만들기
    # 지도 밖 체크를 벽 체크로 바꾸기 위해서 패딩을 사용함.
    new_board = [[1] * (n + 2) for _ in range(n+2)]
    for r in range(n):
        for c in range(n):
            new_board[r+1][c+1] = board[r][c]
    #로봇의 좌표 초기값
    start = ((1, 1), (1, 2))
    # 3. BFS 준비

    # BFS에서 사용할 큐를 만든다.
    # 큐는 "앞으로 탐색할 로봇 상태들"을 담는 대기줄이다.
    q = deque()

    # 시작 상태를 큐에 넣는다.
    # start = 로봇의 시작 위치
    # 0 = 시작 위치까지 걸린 시간
    # 즉, "현재 로봇은 start 위치에 있고, 아직 0초가 걸렸다"는 뜻이다.
    q.append((start, 0))

    # 이미 방문한 로봇 상태를 저장할 set을 만든다.
    # 같은 위치를 반복해서 탐색하지 않기 위해 사용한다.
    visited = set()

    # 시작 위치는 이미 방문했다고 기록한다.
    # sorted(start)를 쓰는 이유:
    # ((1,1), (1,2))와 ((1,2), (1,1))은 같은 로봇 상태이기 때문이다.
    # tuple로 바꾸는 이유:
    # set에는 리스트 같은 변경 가능한 값은 넣을 수 없고, tuple은 넣을 수 있기 때문이다.
    visited.add(tuple(sorted(start)))

    # 4. BFS 실행

    # 큐에 탐색할 상태가 남아 있는 동안 계속 반복한다.
    while q:

        # 큐에서 가장 먼저 들어온 상태를 하나 꺼낸다.
        # pos = 현재 로봇 위치
        # time = 현재 위치까지 걸린 시간
        pos, time = q.popleft()

        # 로봇이 차지하는 두 칸 중 하나라도 도착점이면 탐색 종료.
        # 패딩 board 기준 도착점은 (n, n)이다.
        if (n, n) in pos:
            # BFS는 가까운 거리부터 탐색하므로,
            # 처음 도착했을 때의 time이 최소 시간이다.
            return time

        # 현재 위치 pos에서 이동/회전으로 갈 수 있는 다음 위치들을 하나씩 확인한다.
        for next_pos in get_next(pos, new_board):

            # 로봇의 두 칸 순서를 정렬해서 방문 체크용 형태로 만든다.
            # 예: ((1,2), (1,1))도 ((1,1), (1,2))와 같은 상태로 처리하기 위해서.
            normalized = tuple(sorted(next_pos))

            # 아직 방문하지 않은 로봇 상태라면
            if normalized not in visited:
                # 방문했다고 기록한다.
                visited.add(normalized)

                # 다음 탐색 대상으로 큐에 넣는다.
                # next_pos = 다음 로봇 위치
                # time + 1 = 이동 또는 회전을 한 번 했으므로 1초 증가
                q.append((next_pos, time + 1))

def get_next(pos, board):
    next_pos = []

    (r1, c1), (r2, c2) = pos

    # 1. 상하좌우 이동
    moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for dr, dc in moves:
        nr1, nc1 = r1 + dr, c1 + dc
        nr2, nc2 = r2 + dr, c2 + dc

        if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
            next_pos.append(((nr1, nc1), (nr2, nc2)))

    # 2. 회전

    # 2-1. 가로 상태
    if r1 == r2:
        # 위쪽 두 칸이 비어 있으면 위로 회전 가능
        if board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:
            # A 기준 위 회전
            next_pos.append(((r1, c1), (r1 - 1, c1)))

            # B 기준 위 회전
            next_pos.append(((r2, c2), (r2 - 1, c2)))

        # 아래쪽 두 칸이 비어 있으면 아래로 회전 가능
        if board[r1 + 1][c1] == 0 and board[r2 + 1][c2] == 0:
            # A 기준 아래 회전
            next_pos.append(((r1, c1), (r1 + 1, c1)))

            # B 기준 아래 회전
            next_pos.append(((r2, c2), (r2 + 1, c2)))

    # 2-2. 세로 상태
    else:
        # 왼쪽 두 칸이 비어 있으면 왼쪽으로 회전 가능
        if board[r1][c1 - 1] == 0 and board[r2][c2 - 1] == 0:
            # A 기준 왼쪽 회전
            next_pos.append(((r1, c1), (r1, c1 - 1)))

            # B 기준 왼쪽 회전
            next_pos.append(((r2, c2), (r2, c2 - 1)))

        # 오른쪽 두 칸이 비어 있으면 오른쪽으로 회전 가능
        if board[r1][c1 + 1] == 0 and board[r2][c2 + 1] == 0:
            # A 기준 오른쪽 회전
            next_pos.append(((r1, c1), (r1, c1 + 1)))

            # B 기준 오른쪽 회전
            next_pos.append(((r2, c2), (r2, c2 + 1)))

    return next_pos

def run_tests():
    # 프로그래머스 예제
    board1 = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    assert solution(board1) == 7
    print("test 1 passed")

    # 장애물 없는 3x3
    board2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert solution(board2) == 3
    print("test 2 passed")

    # 장애물 없는 4x4
    board3 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    assert solution(board3) == 5
    print("test 3 passed")

    print("all tests passed")


run_tests()