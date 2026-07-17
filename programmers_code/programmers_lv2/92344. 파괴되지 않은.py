# 정확성과 효율성 테스트
# n x m 게임맵
# (r1, c1) ~ (r2, c2)
# board 건물의 내구도
# skill은 적의 공격 또는 아군의 회복 스킬
# skill의 각 행은 [type, r1, c1, r2, c2, degree]
# type = 1이면 적의 공격, 건물의 내구도 낮춤, degree만큼
# type =2이면 아군 회복, 건물의 내구도 향상, degree만큼
# 적의 공격 내구도 감소, 내구도 0이하 파괴, 공격을 받으면 계속해서 내구도 하락
# 회복스킬로 내구도 향상
# 1 이상이 되면 파괴되지 않은 건물 상태
# 파괴되지 않은 건물의 수 return

# 범위 업데이트가 많다
# 직사각형 전체에 같은 값을 더하거나 뺀다
# # 마지막 결과만 필요하다
# 범위 변화량을 따로 기록하고
# 마지막에 한 번에 누적해서 board에 반영

# 슈도코드
def solution(board, skill):
    # 1. board크기를구한다.
    n = len(board)
    m = len(board[0])

    #2. diff 배열을 만든다. 처음에는 값이 없어서 0으로 초기화한다.
    diff = [[0]* (m + 1) for _ in range(n + 1)]

    #3. skill을 하나씩 본다.
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        else:
            degree = degree

        diff[r1][c1] += degree
        diff[r1][c2 +1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2 +1] += degree

    #4. diff를 가로 누적한다.
    for y in range(n):
        for x in range(1, m):
            #왼쪽값을 더함
            diff[y][x] += diff[y][x-1]

    #5. diff를 세로 누적한다.
    for x in range(m):
        for y in range(1, n):
            #위쪽값을 더함.
            diff[y][x] += diff[y-1][x]

    #6. board에 diff값을 더해서 살아있는 값을 센다.
    answer = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] + diff[y][x] > 0:
                answer +=1
    #7. answer 반환
    return answer

print(solution(
    [[5, 5, 5, 5, 5],
     [5, 5, 5, 5, 5],
     [5, 5, 5, 5, 5],
     [5, 5, 5, 5, 5]],
    [[1, 0, 0, 3, 4, 4],
     [1, 2, 0, 2, 3, 2],
     [2, 1, 0, 3, 1, 2],
     [1, 0, 1, 3, 3, 1]]
))  # 10


print(solution(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    [[1, 1, 1, 2, 2, 4],
     [1, 0, 0, 1, 1, 2],
     [2, 2, 0, 2, 0, 100]]
))  # 6