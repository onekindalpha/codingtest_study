# 두 지역간 길 통과 걸리는 시간 모두 1
# 지도 정보로 최단 시간 부대 복귀
# 다만, 돌아오는 경로 없어져, 복귀 불가능도 있을 수 있음

# 총지역 수 n, 두 지역 왕복 길 roads, 서로 다른 지역들 sources, 강철부대지역 destination
# sources의 원소순서대로 강철부대로 복귀가능한 최단시간 담은 배열
# 복귀 불가능한 경우 해당 부대원 최단시간 -1

# sources의 원소가 각각 1로 가는데 걸리는 최단시간을 알아야 함.
# roads에는 두 지역간 왕복으로 연결된 배열을 알 수 있음.
from collections import deque

def solution(n, roads, sources, destination):
    # graph[i] = i번 지역과 연결된 지역 목록
    graph = [[] for _ in range(n + 1)]

    # roads에 있는 길을 graph에 저장
    # 길은 양방향이라서 a -> b, b -> a 둘 다 저장
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # visited[i] = i번 지역을 BFS로 방문했는지
    visited = [False] * (n + 1)

    # distance[i] = i번 지역에서 destination까지 필요한 길 개수
    distance = [0] * (n + 1)

    # BFS 시작 지역은 destination
    visited[destination] = True
    distance[destination] = 0

    # 앞으로 검사할 지역 목록
    q = deque([destination])
    # 큐에 검사할 지역이 남아 있는 동안 BFS 실행
    while q:
        # 큐 맨 앞 지역을 꺼낸다
        now = q.popleft()

        # now 지역과 연결된 지역들을 하나씩 본다
        for nxt in graph[now]:

            # nxt 지역을 아직 방문하지 않았다면
            if visited[nxt] == False:

                # nxt 지역 방문 처리
                visited[nxt] = True

                # nxt 지역에서 destination까지 거리 저장
                # now까지 거리 + 길 1개
                distance[nxt] = distance[now] + 1

                # nxt 지역과 연결된 지역들도 봐야 하므로 큐에 넣는다
                q.append(nxt)

    # sources별 정답 저장
    answer = []

    for s in sources:
        # s 지역을 방문하지 못했다면 destination까지 갈 수 없음
        # # 길이 양방향이므로 destination에서 s를 방문하지 못했다면 s에서 destination도 갈 수 없다.
        if visited[s] == False:
            answer.append(-1)

        # s 지역을 방문했다면 distance[s]가 최단거리
        else:
            answer.append(distance[s])
    return answer


print(solution(
    3,
    [[1, 2], [2, 3]],
    [2, 3],
    1
))
# [1, 0]


print(solution(
    5,
    [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],
    [1, 3, 5],
    5
))
# [2, -1, 0]


print(solution(
    5,
    [[1, 2], [2, 3], [3, 4]],
    [1, 2, 3, 4, 5],
    3
))
# [2, 1, 0, 1, -1]