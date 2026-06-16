# N개의 마을이 있고, 마을 번호는 1번부터 N번까지다.
# 도로는 양방향으로 통행할 수 있다.
# 도로마다 걸리는 시간이 다르다.
# => 가중치가 있는 양방향 그래프

# road는 인접행렬이 아니라 간선 리스트다.
# road의 각 원소 [a, b, c]는
# a번 마을과 b번 마을이 c시간짜리 도로로 연결되어 있다는 뜻이다.

# 1번 마을에서 시작해서 각 마을까지의 최단 시간을 구해야 한다.
# => 다익스트라
# 1. 시작점에서 각 마을까지의 최단거리 표를 만든다.
# 2. 처음에는 시작점만 0, 나머지는 무한대로 둔다.
# 3. 가장 가까운 마을을 하나 꺼낸다.
# 4. 그 마을을 거쳐서 다른 마을로 가는 시간이 더 짧으면 갱신한다.
# 5. 이 과정을 반복한다.
# 최단 시간이 K 이하인 마을의 개수를 return한다.
import heapq
def solution(N, road, K):
    answer = 0

    # 1. road 간선 리스트를 인접 리스트 graph로 바꾸기
    graph = [[] for _ in range(N+1)]
    # ex. graph = [[], [], [], [], [], []]

    for a, b, c in road:
        # 양방향이라고 했으므로.
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 2. 1번 마을에서 각 마을까지의 최단 시간 표 만들기
    INF = int(1e9)
    distance = [INF] * (N+1)
    distance[1] = 0

    # 3. 우선순위 큐에 시작 마을 넣기.  해당 큐에는 (현재까지 걸린 시간, 마을 번호) 형태로 넣음.
    # 앞으로 확인할 마을들 우선순위 큐에 담기.
    pq = []
    # heapq는 pq라는 우선순위 큐에 값을 넣는 것을 도와줌.
    heapq.heappush(pq, (0, 1))
    # current_cost =0, current_village =1
    # 4. 우선순위 큐에서 현재까지 가장 가까운 마을을 꺼내기.
    while pq:
        # heapq.heappop(pa)는 그중 걸린 시간이 가장 작은 값을 꺼낸다.
        current_cost, current_village = heapq.heappop(pq)
        if current_cost > distance[current_village]:
            continue
        # 현재 마을에서 바로 갈 수 있는 다음 마을들을 하나씩 확인한다.
        # current_village=1, ex. graph[1] = [(2, 1), (4, 2)]
        for next_village, cost in graph[current_village]:
            # ex. next_village =2, cost =1
            new_cost = current_cost + cost
            # ex. new_cost = 1
            if new_cost < distance[next_village]:
                distance[next_village] = new_cost
                # next_village도 new_cost시간으로 갈 수 있게 되었음.
                heapq.heappush(pq, (new_cost, next_village))

    for d in distance[1:]:
        if d <= K:
            answer += 1
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# 4

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
# 4