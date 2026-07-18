# n개의 노드. 각 노드는 1번부터 n번
# 양방향 통행이 가능한 등산로로 연결. 일정 시간이 소요됨.
# 각 노드는 출입구, 쉼터, 혹은 산봉우리임.
# 등산코스는 방문할 노드 번호들을 순서대로 나열하여 표현.
# 쉼터 혹은 산봉우리를 방문할때마다 휴식 취할 수 있음
# 휴식 없이 이동해야 하는 시간 중 가장 비용이 큰걸 해당 등산코스의 intnesity

# 규칙: 출입구에서 출발하여, 산봉우리 중 한 곳만 방문하고, 원래 출입구로 돌아오는 코스를ㄹ 정하려고 함.
# 이러한 규칙을 지키는 동시에, intensity(그러니까, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간이)
# 최소가 되도록 등산코스를 정하려고 함.
# 각 선분에는 등산로 이동시간이 있음.

# 노드 수 n, 등산로 정보 담은 2차원 정수 배열 paths
# 출입구 번호 담긴 정수 배열 gates
# 산봉우리들 번호 담긴 정수배열 summits
# intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호와
# intensity의 최솟값을 차례대로 정수 배열에 담아 return하도록
# 만약 intensity가 최소가 되는 등산코스가 여러개라면 그중 산봉우리 번호가 가장 낮은 등산코스 선택

# paths의 원소는 [i, j, w] # 노드와 노드를 연결하는 간선존재, 그리고 걸리는 시간
# gates와 summits에 등장하지 않은 노드는 모두 쉼터
# 임의의 두 지점 사이 이동가능 경로 항상 존재

# 최소비용을 구하는데 유리한, 다익스트라 문제. 간선비용이 0 이상일 때 사용. 빠름. 우선순위 큐 사용. 최단거리 문제에서 많이 사용.

import heapq

#문답을 통해 알아낸 clue
#1. 출입구 → 산봉우리까지의 최소 intensity를 구한다.
#2. intensity는 경로에서 지나간 간선 비용 중 최댓값이다.
#3. 내려오는 길은 따로 생각하지 않는다. 더 좋은 길이면 올라갈 때도 계산된다고 본다.
#4. 최소 intensity를 갱신해가는 문제라 다익스트라 변형을 쓴다.
#5. 정답은 산봉우리 번호와 최소 intensity 값이다.

# 1.  그래프를 만든다.
def build_graph(n, paths):
    graph = [[] for _ in range(n + 1)]
    # ex. paths = [i, j, w]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
    return graph

def dijkstra(graph, gate_set, summit_set, n):
    #3. intensity 배열 만들기. 의미는 각 노드까지의 최소 intensity.
    INF = int(1e9)
    # intensity의 배열을 만듦. 인덱스는 노드번호.
    intensity = [INF] * (n+1)
    #우선순위 큐를 만든다.
    q = []
    for gate in gate_set:
        intensity[gate] = 0
        #출발지점들은 아직 이동을 안했으므로 비용이 0이고
        #추후에 비용이 가장 작은 노드부터 꺼내려고 한다면
        #heapq는 튜플의 첫번째 값 기준으로 작은 것부터 꺼내기 때문에
        # intensity와 출발점
        heapq.heappush(q, (0, gate))

    #q가 비어있지 않으면
    while q:
        #왜 여기서는 popleft안하지
        # 현재까지 intensity와 현재 노드
        current_intensity, current_node = heapq.heappop(q)
        # 힙에 남아 있는 오래된 나쁜 값을 스킵하는 코드
        if current_intensity > intensity[current_node]:
            continue
        #산봉우리에 도착했으면, 거기서 더 이상 이동하지 않는다.
        if current_node in summit_set:
            continue
        # 다음에 갈 노드가 출입구인지 검사함.
        for next_node, w in graph[current_node]:
            if next_node in gate_set:
                continue
            #next_node까지 갔을 때의 intensity 후보를 계산함
            next_intensity = max(current_intensity, w)
            #기존에 알고 있던 next_node까지의 intensity보다 더 작으면 갱신함
            if next_intensity < intensity[next_node]:
                intensity[next_node] = next_intensity
                # 갱신된 상태를 우선순위 큐에 넣음
                heapq.heappush(q, (next_intensity, next_node))
    return intensity

def solution(n, paths, gates, summits):
    graph = build_graph(n, paths)

    #2. gate_set, summit_set 만들기
    gate_set = set()
    summit_set = set()
    for gate in gates:
        gate_set.add(gate)
    for summit in summits:
        summit_set.add(summit)

    #4. dijkstra돌리기
    intensity = dijkstra(graph, gate_set, summit_set, n)

    #5. answer고르기
    summits.sort()
    # 정렬된 산봉우리 중 첫 번째를 일단 정답 후보로 잡는다.
    answer_summit = summits[0]
    answer_intensity = intensity[summits[0]]
    # 그 다음 산봉우리부터 보면서 intensity가 더 작으면 교체한다.
    for summit in summits[1:]:
        # intensity[summit]는 산봉우리까지 갈때 가능한 최소 intensity
        #같으면 교체하지 않는다.
        if intensity[summit] < answer_intensity:
            answer_summit = summit
            answer_intensity = intensity[summit]

    return [answer_summit, answer_intensity]


def test_pick_answer():
    INF = int(1e9)

    summits = [5, 3, 7]

    intensity = [INF] * 8
    intensity[3] = 6
    intensity[5] = 4
    intensity[7] = 4

    summits.sort()

    answer_summit = 0
    answer_intensity = INF

    for summit in summits:
        if intensity[summit] < answer_intensity:
            answer_summit = summit
            answer_intensity = intensity[summit]

    assert [answer_summit, answer_intensity] == [5, 4]
    print("통과:", [answer_summit, answer_intensity])
