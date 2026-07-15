#nxm
from ctypes.macholib import dyld


# (x, y) -> (r, c)

# 이동 거리가 총 k, 위 두개 격자를 포함해,, 같은 격자를 두 번 이상 방문해도 됨
# 탈출한 경로를 문자열로 나타냈을때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 함.

# 핵심: 사전순으로 가장 빠른 경로를 찾아야 함. 그래서 이동 방향을 d, l, r,u순서로 시도한다.
# 맨해튼 거리는 격자에서 상하좌우로만 움직일 때 필요한 최소 이동 횟수임
# dist = abs(x-r) + abs(y-c) <-세로로 몇 칸 차이인지 가로로 몇 칸 차이인지
# 그래서 그리디임. 앞 글자를 가장 작은 문자로 확정해나가니까.
# 가지치기는 어차피 답이 안되는 길은 탐색하지 않는 것임.

# 격자 밖으로 나가면 안되고,
# 남은 이동 횟수로 도착점까지 갈 수 있어야 하고,
# 남은 거리와 남은 횟수의 홀짝이 맞아야 함. -> 즉, 최소 거리보다 남는 횟수가 짝수여야 함. 같은 격자를 두번이상 방문해도 되니까.

# l:왼쪽으로 한 칸 이동
# r:오른쪽으로 한 칸 이동
# u:위쪽으로 한 칸 이동
# d:아래쪽으로 한 칸 이동

# 미로에서는 인접한 상, 하, 좌, 우 격자로 한칸씩 이동 가능

# 좌측상단 (1, 1), 우측 하단은 (3, 4)
# .은 빈 공간, S는 출발 지점, E는 탈출 지점임

# 격자 크기 n, m
# 출발위치 x, y
# 탈출지점 r, c

# 탈출가지 이동해야 하는 거리 k

# 미로를 탈출하기 위한 경로 result

# 위 조건대로 미로를 탈출할 수 없는 경우: "

def solution(n, m, x, y, r, c, k):
    answer = []
    #처음부터 불가능한지 확인. 가지치기.
    dist = abs(x - r) + abs(y - c)
    if dist > k:
        return "impossible"
    # 도착하고 남는 이동횟수가 짝수면 가능, 홀수면 불가능.
    if (k - dist) % 2 != 0:
        return "impossible"

    # 매번 d, l, r, u순서로 확인:
    #행과 열 순
    directions = [
        ("d", 1, 0),
        ("l", 0, -1),
        ("r", 0, 1),
        ("u", -1, 0)
    ]
    # 현재 위치에서 k번 동안 이동
    for step in range(k):
        for move, dx, dy in directions:
            # 다음 위치
            nx = x + dx
            ny = y + dy
            # 다음 위치가 격자 안인지 확인
            if 1 <= nx <= n and 1 <= ny <= m:
                #이 방향은 일단 가능
                #다음 위치에서 도착점까지의 남은 거리 계산
                dist = abs(nx -r) + abs(ny - c)
                remain = k - step - 1

                # 남은 이동 횟수로 도착 가능한지 확인
                # 도착하고 남는 횟수를 왕복으로 소모 가능한지?
                if dist <= remain and (remain - dist) %2 == 0:
                    #그럼 그 방향은 가능
                    answer.append(move)
                    # 그렇다면 위치 갱신
                    x = nx
                    y = ny
                    # 가능하면 일단 다음 step으로 넘어감.
                    break

    #끝까지 만들면 경로 return
    return "".join(answer)

print(solution(3, 4, 2, 3, 3, 1, 5))
# 기대값: "dllrl"

print(solution(2, 2, 1, 1, 2, 2, 2))
# 기대값: "dr"

print(solution(3, 3, 1, 2, 3, 3, 4))
# 기대값: "impossible"

print(solution(3, 3, 1, 1, 1, 1, 2))
# 기대값: "du" 또는 가능한 사전순 경로

print(solution(3, 3, 1, 1, 3, 3, 4))
# 기대값: "ddrr"

