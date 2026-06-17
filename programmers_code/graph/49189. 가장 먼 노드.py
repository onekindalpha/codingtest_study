# 1. 1번 노드에서 시작한다.
# 2. 간선은 양방향이다.
# 3. 가장 멀리 떨어진 노드는 “최단거리 기준으로 간선 개수가 가장 많은 노드”다.
# 4. 모든 간선의 비용은 동일하게 1이다.
# 5. 따라서 1번 노드에서 BFS를 돌려 각 노드까지의 최단거리를 구한다.
# 6. 최단거리 배열에서 가장 큰 값을 찾는다.
# 7. 그 최댓값을 가진 노드 개수를 return 한다.

# 1번 노드에서 모든 노드까지의 최단거리, 즉 간선 개수를 구해야 한다.
# 간선은 양방향이므로 graph[a].append(b), graph[b].append(a)로 저장한다.
# 간선 개수를 기준으로 한 최단거리 문제이므로 거리 배열이 필요하다.
# 모든 간선의 비용이 동일하게 1로 취급되므로 BFS로 최단거리를 구할 수 있다.
# 거리 배열에서 가장 큰 값을 찾고, 그 값을 가진 노드 개수를 센다.

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 각 노드까지의 최단거리 기록표 세팅
    distance = [-1] * (n+1)
    #1번에서 1번까지 거리 0
    distance[1] = 0
    # 탐색 후보 시작점.
    queue = deque([1])
    # 큐를 계속 탐색할건데
    while queue:
        # 맨앞의 큐를 꺼내라.
        current = queue.popleft()
        # 연결된 노드를 확인했을때
        for next_node in graph[current]:
            # 아직 방문을 안한 노드면
            if distance[next_node] == -1:
                # 현재거리에서 1을 더해서 거리 정보를 저장.
                distance[next_node] = distance[current] + 1
                # 새로 발견한 노드를 다음 탐색 후보에 넣음.
                queue.append(next_node)
    #BFS가 끝나면 distance에는 1번 노드에서 각 노드까지의 최단 거리가 들어있음.
    # ex. distance = [-1, 0, 1, 1, 2, 2, 2]
    # 실제 노드면 1번부터 n번까지만 짜름.
    real_distances = distance[1:]
    # 실제 노드들 중 가장 먼 거리값을 찾는다.
    max_distance = max(distance[1:])
    # 그 가장 먼 거리값을 가진 노드가 몇 개인지 센다. list.count(찾고싶은값)
    answer = real_distances[1:].count(max_distance)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))