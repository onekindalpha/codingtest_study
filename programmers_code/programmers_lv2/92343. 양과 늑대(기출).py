# 이진트리 모양
# 목적: 양 모으기
# 특이점: 각 노드를 방문할 때마다 해당 노드에 있던 양과 늑대가 나를 따라옴
# 특이점2: 늑대는 양을 노림, 만약 양보다 늑대수가 같거나 많아지면 모든 양을 다 먹음
# 결론: 나는 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트노드로 돌아오는 것
# 첨언: 루트노드에는 항상 양이 있으므로, 0번 노드에서 출발하면 양을 1마리 모음.
from os import WCONTINUED
# 각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info
# 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges
# 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양이 최대 몇마리인지
# 양과 늑대 문제는 “현재 갈 수 있는 후보 노드들” 중 하나를 선택하는 DFS/백트래킹 문제다.

def solution(info, edges):
    # 1. 자식 정보를 담은 tree를 만든다.
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)
    answer = 0
    # 2. dfs 함수 정의
    def dfs (current_sheep, current_wolf, next_nodes):
        nonlocal answer
        #현재까지 모은 양 수로 정답 갱신
        answer = max(answer, current_sheep)
        #후보 노드들 중 하나를 고른다.
        for next_node in next_nodes:
        #3. next_node가 양인지 늑대인지 확인
            if info[next_node] == 0: #양
                new_sheep = current_sheep + 1
                new_wolf = current_wolf
            else: #늑대
                new_sheep = current_sheep
                new_wolf = current_wolf + 1

            #4. 늑대가 양 이상이면 이 선택지는 실패
            if new_wolf >= new_sheep:
                continue
            #5. 다음 후보 목록 만들기
            new_next_nodes = next_nodes.copy()
            # 방금 방문한 노드는 후보에서 제거한다.
            new_next_nodes.remove(next_node)
            # 방금 방문한 노드의 자식들을 후보에 추가한다.
            new_next_nodes.extend(tree[next_node])

            # 새로 바뀐 후보로 재탐색
            dfs(new_sheep, new_wolf, new_next_nodes)

    #dfs시작 호출
    dfs(1, 0, tree[0])

    return answer

# 테스트 코드 1
print(solution(
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10],
     [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
))  # 5


# 테스트 코드 2
print(solution(
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
     [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
))  # 5