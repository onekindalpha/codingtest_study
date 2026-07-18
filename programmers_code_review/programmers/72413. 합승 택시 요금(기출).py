# 지점의 개수 n
# 출발지점을 나타내는 s
# A의 도착지점을 나타내는 a
# B의 도착지점을 나타내는 b
# 지점 사이의 예상 택시요금을 나타내는 fares
# 답: 최저 예상 택시요금
# 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됨

# 출발지점과 a의 도착지점, b의 도착지점은 서로 겹치지 않음
# fares는 2차원 정수 배열
# 1. 지도 만든다.
# 2. s에서 출발하는 최단거리표 만든다.
# 3. a에서 출발하는 최단거리표 만든다.
# 4. b에서 출발하는 최단거리표 만든다.
# 5. 모든 지점을 “헤어지는 지점 x”라고 가정해본다.
# 6. s→x + x→a + x→b 비용 중 최솟값을 고른다.
import heapq

# s에서 x까지 비용, x에서 a까지 비용, x에서 b까지 비용
# dist_s[x]+ dist_a[x] + dist_b[x]

def solution(n, s, a, b, fares):
    INF = int(1e15)
    #그래프를 만든다.
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        # 양방향으로 갈 수 있고, 비용은 f다.
        graph[c].append((d, f))
        graph[d].append((c, f))
    # 다익스트라
    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            current_cost, current_node = heapq.heappop(heap)
            if current_cost > dist[current_node]:
                continue

            for next_node, next_cost in graph[current_node]:
                new_cost = current_cost + next_cost

                if new_cost < dist[next_node]:
                    dist[next_node] = new_cost
                    heapq.heappush(heap, (new_cost, next_node))

        return dist
    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    answer = INF

    for x in range(1, n+1):
        cost = dist_s[x] + dist_a[x] + dist_b[x]
        answer = min(answer, cost)

    return answer
# 테스트 코드

print(solution(
    6, 4, 6, 2,
    [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25]
    ]
))  # 82

print(solution(
    7, 3, 4, 1,
    [
        [5, 7, 9],
        [4, 6, 4],
        [3, 6, 1],
        [3, 2, 3],
        [2, 1, 6]
    ]
))  # 14

print(solution(
    6, 4, 5, 6,
    [
        [2, 6, 6],
        [6, 3, 7],
        [4, 6, 7],
        [6, 5, 11],
        [2, 5, 12],
        [5, 3, 20],
        [2, 4, 8],
        [4, 3, 9]
    ]
))  # 18