# 아, 최단거리 문제구나. 시작 노드에서 다른 모든 노드까지 최소 비용을 구하는 문제구나. 
# 주어진 것은 시작노드 start, 노드의 개수 numNodes, 간선정보 edges.
# edges를 인접 리스트로 바꿔야 겠다. (ex.[0,1,9]는 0: (1,9)로 저장할 수 있음.)
# 뱡향이 있음. adj[출발노드].append((도착노트, 비용)))
# 각 노드까지의 최소 비용을 저장할 배열 만들기.
# 일반 큐 아니고, 우선순위 큐(pq)에 시작 노드 넣기: 아직 확인할 후보 중에서 현재 비용이 가장 싼 노드부터 꺼낸다. 

import heapq

def solution(start, numNodes, edges):
    adj = {}
    for from_node,to_node,cost in edges:
        if from_node not in adj:
            adj[from_node] = []
        adj[from_node].append((to_node, cost))
    
    INF = float('inf')
    dist = [INF] * numNodes
    dist[start] = 0
    # dist = [0, inf, inf]
    # 앞으로 확인할 노드 후보를 담을 빈 상자.
    # (0, 0) : (현재 비용, 노드 번호) -> 비용 0으로 0번 노드에 도착할 수 있다.
    # ex. pq = 우선순위 큐

    # 다익스트라는 매번 현재 후보 중 비용이 가장 작은 노드부터 확인해야 한다.
    # 그래서 pq에 (비용, 노드) 형태로 넣는다.

    # 예:
    # (9, 1) = 1번까지 비용 9
    # (3, 2) = 2번까지 비용 3

    # pq는 비용이 작은 (3, 2)를 먼저 꺼낸다.
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_cost > dist[current_node]:
            continue
        
        for next_node, cost in adj.get(current_node, []):
            new_cost = current_cost + cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    return dist

print(solution(
    0,
    3,
    [[0, 1, 9], [0, 2, 3], [1, 0, 5], [2, 1, 1]]
))

print(solution(
    0,
    4,
    [[0, 1, 1], [1, 2, 5], [2, 3, 1]]
))