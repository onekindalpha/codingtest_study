# 벨만 포드 알고리즘. 음수 가중치도 가능한 최단 거리 알고리즘.
# num_vertices 정점의 개수. edges 간선정보. sources 시작 정점.
# 방문 순서가 아니라, 시작 노드에서 다른 노드들까지 최소 비용을 구하는 문제임. 
# 시작 정점, 끝 정점, 가중치
# edges의 [a, b, c]는 a에서 b로 비용 c로 이동한다는 뜻이군. 
# source는 시작 노드이므로, source에서 모든 노드까지의 최단 거리를 구해야겠군. 

# dist= 최저가격표이니, dist 배열을 만든 뒤, 모든 간선을 반복해서 검사해야겠군. 
# 간선 [a, b, c]를 볼 때, a까지의 최소 비용 + c가 b까지의 기존 비용보다 적으면 갱신하면 되게ㅆ군. 
def solution(num_vertices, edges, source):

    INF = 99999
    # 처음에는 모든 노드까지의 비용을 모른다고 보고 INF로 초기화한다. 
    dist = [INF] * num_vertices
    dist[source] = 0
    # 시작 노드 source까지의 비용은 0으로 둔다. 

    # 모든 간선을 여러 번 보면서, 더 싼 길이 발견되면 dist를 계속 고친다. 

    for _ in range(num_vertices -1):
        for a, b, c in edges:
            if dist[a] != INF and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c

    # 마지막으로 한번 더, 음의 순환을 확인할 것. 
    for a, b, c in edges:
        if dist[a] != INF and dist[a] + c < dist[b]:
          # 음의 순환이 존재한다는 뜻이므로, 예외 처리한다. 
            return [-1]
        
        # 음의 순환이 없으면 최단거리 반환
    return dist

print(solution(
    5,
    [[0, 1, 4], [0, 2, 3], [0, 4, -6], [1, 3, 5],
     [2, 1, 2], [3, 0, 7], [3, 2, 4], [4, 2, 2]],
    0
))

print(solution(
    4,
    [[0, 1, 5], [0, 2, -1], [1, 2, 2],
     [2, 3, -2], [3, 0, 2], [3, 1, 6]],
    0
))