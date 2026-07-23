# BFS 최단거리 문제
# 숫자를 노드로 보고, +n / *2 / *3 연산을 간선으로 본다.
# 연산 1번 = 거리 1칸

from collections import deque

def solution(x, y, n):
    # distance[num] = x에서 num까지 가는 데 필요한 최소 연산 횟수
    # -1 = 아직 방문하지 않은 숫자
    distance = [-1] * (y + 1)

    # BFS에서 사용할 큐
    q = deque()

    # 시작 숫자 x를 큐에 넣는다
    q.append(x)

    # x에서 x까지는 연산을 하지 않았으므로 0
    distance[x] = 0

    # 큐가 빌 때까지 탐색
    while q:
        # 먼저 들어온 숫자부터 꺼낸다
        now = q.popleft()

        # 현재 숫자에서 한 번의 연산으로 만들 수 있는 다음 숫자들
        for nxt in [now + n, now * 2, now * 3]:

            # y보다 큰 숫자는 목표를 넘어가므로 제외
            # distance[nxt] == -1 은 아직 방문하지 않았다는 뜻
            if nxt <= y and distance[nxt] == -1:

                # nxt까지의 최소 연산 횟수는
                # now까지의 연산 횟수 + 현재 연산 1번
                distance[nxt] = distance[now] + 1

                # 다음 탐색 대상으로 큐에 넣는다
                q.append(nxt)

    # y까지 도달했다면 최소 연산 횟수
    # 도달하지 못했다면 초기값 -1 그대로 반환
    return distance[y]

    print(solution(10, 40, 5))
    # 2

    print(solution(10, 40, 30))
    # 1

    print(solution(2, 5, 4))
    # -1

    print(solution(1, 10, 1))
    # 3