# 너비 우선 탐색
# graph, start가 주어지는 군. graph는 간선이고, 인접리스트로 바꾸어야 겠군.
# 방향 없는 그래프라는 말이 없어!
# 큐를 만들어야겠군. 
# start에서 출발해서 queue에 넣고, 방문처리하고, queue에서 하나씩 꺼내서, 꺼낸 노드의 이웃 중 안 간 노드를 순서대로 줄세워서, queue에 넣어야 겠군. 
# 차례대로 방문해서, 방문 순서를 return해야겠군.

from collections import deque
def solution(graph, start):
    adj = {}

    #1. 인접리스트 만들어야겠군
    for a, b in graph:
        if a not in adj:
            adj[a] = []
        if b not in adj:
            adj[b] = []
    
         # 문제에서 [출발 노드, 도착 노드] 라고 했으므로 한쪽 방향만 저장. 
        adj[a].append(b)
    
    visited = set()
    answer = []

    #2. BFS 함수 만들기
    queue = deque([start])
    # 큐에 넣는 순간 방문 처리함. 
    visited.add(start)
    answer.append(start)

    while queue:
        node = queue.popleft()

        for next_node in adj[node]:
            if next_node not in visited:
                visited.add(next_node)
                answer.append(next_node)
                queue.append(next_node)
    return answer

print(solution(
    [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],
    1
))

print(solution(
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],
    1
))
