# 문제 키워드: 깊이 우선 탐색 순회
# 문제 인식: 그래프와 시작노드가 주어졌을때, DFS가 방문한 순서를 반환하라. 
# 문제 정의: start에서 출발해서 DFS 방문 순서를 answer에 담는 문제이군.
# 반환값은 방문 순서, graph는 간선목록이군. 간선목록을 인접 리스트 만들어야지. 
# 방향없는 그래프라고 했으니, 양쪽에 저장해야지 
# DFS 방문 순서 문제면, visited와 answer 리스트는 필수겠군. 
# DFS의 행동은 (1) 현재 노드 방문 처리 (2) answer에 현재 노드 추가 (3) 현재 노드의 이웃을 하나씩 확인 (4) 아직 방문 안 한 이웃이면 dfs를 호출해야겠군. 
# 문제에서 start가 주어졌으니, 마지막은 dfs(start) 호출해서 return answer을 반환하면 되겠군.

def solution(graph, start):
    adj = {}
    for a,b in graph:
        if a not in adj:
            adj[a] = []
        if b not in adj:
            adj[b] = []

        adj[a].append(b)
        adj[b].append(a)

    visited = set() 
    answer = []
    
    def dfs(node):
        visited.add(node)
        answer.append(node)

        for next_node in adj[node]:
            if next_node not in visited:
                dfs(next_node)

    dfs(start)
    return answer 


print(solution(
    [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']],
    'A'
))

print(solution(
    [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']],
    'A'
))

# # 템플릿화

# def solution(graph, start):
#     # 1. 인접 리스트 만들기
#     adj = {}

#     for a, b in graph:
#         # a, b 칸 없으면 만들기

#         # 방향 없는 그래프니까 양쪽 연결하기

#     # 2. 방문 기록, 정답 리스트 만들기
#     visited = set()
#     answer = []

#     # 3. DFS 함수 만들기
#     def dfs(node):
#         # 현재 노드 방문 처리
#         # answer에 넣기
#         # 이웃 노드 확인
#         # 안 갔으면 dfs 호출

#     # 4. 시작 노드에서 DFS 시작
#     dfs(start)

#     # 5. 방문 순서 반환
#     return answer