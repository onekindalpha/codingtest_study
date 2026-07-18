# x + n을 더함
# x에 2를 곱함
# x에 3을 곱함

# x를 y로 변환하기 위해 필요한 최소 연산 횟수
# x를 y로 만들 수 없다면 -1을 return
# BFS 최단거리

from collections import deque

def solution(x, y, n):
    distance = [-1] * (y+1)
    q = deque()
    q.append(x)
    distance[x] = 0

    while q:
        now = q.popleft()

        for nxt in [now + n, now * 2, now * 3]:
            # 목표값 보다 크지 않은지, nxt를 아직 방문하지 않았는지,
            if nxt <= y and distance[nxt] == -1:
                # nxt까지 가는 횟수 = now까지 가는 횟수 + 연산 1번
                distance[nxt] = distance[now] + 1
                # nxt도 다음 검사 대상으로 큐에 넣음.
                q.append(nxt)
    #y까지 가는 최단거리를 리턴
    return distance[y]


print(solution(10, 40, 5))
# 2

print(solution(10, 40, 30))
# 1

print(solution(2, 5, 4))
# -1

print(solution(1, 10, 1))
# 3