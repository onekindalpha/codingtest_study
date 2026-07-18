# 트리를 구성하는 모든 노드의 x, y좌표 값은 정수
# 정렬 + 이진트리 삽입 + DFS 순회
# 이진트리 삽입이란: 새 노드를 넣을 때, 현재 노드보다 x가 작으면 왼쪽, 크면 오른쪽으로 내려가면서 빈자리를 찾아넣는것.
from errno import ECHILD


# 곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수
# 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return
# 노드에 번호 붙이기
# y내림차순, x오름차순 정렬
# 첫번째 노드를 root로 삼기
# 나머지 노드들 x기준으로 삽입
# 전위순회 구하기
# 후위순회 구하기

# Node 하나를 만들 때
# x좌표, y좌표, 번호를 저장하고
# 처음에는 왼쪽 자식도 없고 오른쪽 자식도 없게 만든다.
# 트리를 구성하는 모든 노드의 x, y좌표 값은 정수
# 정렬 + 이진트리 삽입 + DFS 순회
# 이진트리 삽입이란: 새 노드를 넣을 때, 현재 노드보다 x가 작으면 왼쪽, 크면 오른쪽으로 내려가면서 빈자리를 찾아넣는것.

import sys
sys.setrecursionlimit(10**6)


# Node 하나를 만들 때
# x좌표, y좌표, 번호를 저장하고
# 처음에는 왼쪽 자식도 없고 오른쪽 자식도 없게 만든다.
class Node:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.left = None
        self.right = None


# 나머지 노드를 x기준으로 삽입
def insert_node(parent, child):
    # child의 x좌표가 parent의 x좌표보다 작으면 왼쪽으로 간다.
    if child.x < parent.x:
        # 왼쪽자리가 비어 있으면 거기에 넣는다.
        if parent.left is None:
            parent.left = child
        # 왼쪽 자리가 이미 차 있으면, 왼쪽 자식 밑으로 내려간다.
        else:
            insert_node(parent.left, child)

    # child의 x좌표가 parent의 x좌표보다 크면 오른쪽으로 간다.
    else:
        # 오른쪽 자리가 비어 있으면 거기에 넣는다.
        if parent.right is None:
            parent.right = child
        # 오른쪽 자리가 이미 차 있으면, 오른쪽 자식 밑으로 내려간다.
        else:
            insert_node(parent.right, child)


# 전위순회
def preorder(node, result):
    if node is None:
        return

    # 전위순회: 나 -> 왼쪽 -> 오른쪽
    result.append(node.number)
    preorder(node.left, result)
    preorder(node.right, result)


# 후위순회
def postorder(node, result):
    if node is None:
        return

    # 후위순회: 왼쪽 -> 오른쪽 -> 나
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.number)


# 곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수
# 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return
def solution(nodeinfo):
    nodes = []

    # 노드에 번호 붙이기
    for i, node in enumerate(nodeinfo):
        x, y = node

        # 파이썬 인덱스는 0부터 시작하고, 문제의 노드 번호는 1부터 시작하므로 i + 1
        nodes.append([x, y, i + 1])

    # y내림차순, x오름차순 정렬
    nodes.sort(key=lambda node: (-node[1], node[0]))

    # 첫번째 노드를 root로 삼기
    x, y, number = nodes[0]
    root = Node(x, y, number)

    # 나머지 노드들 x기준으로 삽입
    for node in nodes[1:]:
        x, y, number = node
        new_node = Node(x, y, number)
        insert_node(root, new_node)

    # 전위순회 구하기
    pre_result = []
    preorder(root, pre_result)

    # 후위순회 구하기
    post_result = []
    postorder(root, post_result)

    return [pre_result, post_result]

# 테스트 코드
print(solution(
    [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
))
# 예상 출력:
# [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]