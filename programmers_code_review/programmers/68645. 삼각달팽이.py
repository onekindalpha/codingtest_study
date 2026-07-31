

def solution(n):
    # 달팽이 숫자를 채울 n x n 임시 배열
    board = [[0 for _ in range(n)] for _ in range(n)]
    dirs = [
        (1, 0), #아래 : 행이 하나 늘어남
        (0, 1), #오른쪽 : 열이 하나 늘어남
        (-1, -1), #왼쪽 위: 행과 열이 하나씩 줄어듦.
    ]
    r = 0
    c = 0
    direction = 0
    #밑변의 길이와 높이가 n임
    #그냥 길이 1부터 길이 n까지 더하는게 아니라 순서대로 합쳐야 하네
    #아 반시계방향으로 달팽이 채우기를 진행
    # 규칙을 정한다.
    # 방향대로 쭉 가다가, 방향이 안맞으면 틀기.
    # 달팽이가 돌아야 하는 전체 칸 수를 먼저 보기
    for num in range(1, n * (n +1) // 2 +1):
        board[r][c] = num
        #
        dr, dc = dirs[direction]
        nr = r + dr
        nc = c + dc
        # 정삼각형 밖이거나, n에 도달햇으면 멈추기.
        # 다음 것이 정해져있으면 멈추기.
        if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] != 0:
            #방향전환한다.
            direction = (direction + 1) % 3
            dr, dc = dirs[direction]
            nr = r + dr
            nc = c + dc
        #다음 반복에서 사용할 현재 위치를 갱신
        r = nr
        c = nc

    #첫행부터 마지막 행까지 순서대로 합친 새로운 배열을 리턴하기
    answer = []
    for row in board:
        for value in row:
            if value != 0:
                answer.append(value)
    return answer

print(solution(4))

print(solution(5))

print(solution(6))