import sys
input = sys.stdin.readline

#동적으로 노드를 추가하고, 색깔을 변경할 수 있는 명령들을 처리할 수 있는 시스템.
# 처음에는 아무 노드도 없음
# class Tree:
# class colorTree:
#     """
#
#     """
roots = []
nodes = {}
def new_node(m_id, p_id, color, max_depth):
    # 루트일경우에
    if p_id == -1:
        roots.append(m_id)
        nodes[m_id] = {
            "parent": p_id,
            "children": [],
            "color": color,
            "max_depth": max_depth
        }
        return True
    # 루트들이 아닌 경우
    if can_add_node(p_id):
        nodes[m_id] = {
            "parent": p_id,
            "children": [],
            "color": color,
            "max_depth": max_depth
        }
        #자식노드를 추가한다.
        nodes[p_id]["children"].append(m_id)
    return True

def can_add_node(p_id):
    cur_depth = 2
    ancestor_id = p_id
    # 현재 노드가 루트 노드가 아닐때
    while ancestor_id != -1:
        if cur_depth > nodes[ancestor_id]["max_depth"]:
            return False
        ancestor_id = nodes[ancestor_id]["parent"]
        cur_depth += 1
    return True

m_id_subtree = []
def change_color(m_id, new_color, nodes):
    # 나부터 변경
    nodes[m_id]["color"] = new_color
    # 내 자식들도 똑같이 변경
    for child_id in nodes[m_id]["children"]:
        change_color(child_id, new_color, nodes)
    return nodes

def show_color(m_id, nodes):
    cur_color = nodes[m_id]["color"]
    return cur_color

def count_worth(roots, nodes):
    total_worth = 0
    for root_id in roots:
        colors, tree_worth = dfs(root_id, nodes)
        total_worth += tree_worth
    return total_worth

def dfs(node_id, nodes):
    #일단 내 색부터. set는 중복제거가 됨.
    colors = {nodes[node_id]["color"]}
    #내 아래쪽 노드르의 가치 합
    subtree_worth = 0
    for child_id in nodes[node_id]["children"]:
        # 자식의 subtree계산
        child_colors, child_subtree_worth = dfs(child_id, nodes)
        # 자식 subtree의 색들을 내 색 종류에 합침
        colors.update(child_colors)
        # 자식 subtree에서 이미 계산한(제곱해서 더해놓은) 가치들도 더함
        subtree_worth += child_subtree_worth
    # 이제 DFS를 돌았기 때문에  colors에는
    # 나를 루트로 하는 subtree전체 색 종류가 들어있음.
    # 이제 현재 노드의 색 종류가 완성됨
    my_worth = len(colors) ** 2
    # 현재 노드의 제곱값을 서브트리 워스에 추가함.
    subtree_worth += my_worth
    return colors, subtree_worth

def main():
    # Q, m, p가 괭장히 큼. max_depth도 큰 편임.
    # 300과 400 명령어에 대해 결과를 한줄에 하나씩 순서대로 출력함.
    Q = int(input())
    result = []
    for _ in range(Q):
        data = list(map(int, input().split()))
        command = data[0]
        if command == 100:
            m_id = data[1]
            p_id = data[2]
            color = data[3]
            max_depth = data[4]
            # m_id는 새로 추가되는 노드 번호로 항상 새로운 값.
            # p_id는 -1이 아닌 이상 항상 이미 주어진 노드 번호임.
            # 만든 함수 실행(호출) = 지금 입력으로 받은 이 값들을 가지고 해당 함수안의 코드를 실행해라
            new_node(m_id, p_id, color, max_depth)
        elif command == 200:
            m_id = data[1]
            new_color = data[2]

            change_color(m_id, new_color, nodes)
            # 이는 m_id는 이미 주어진 노드 번호만 주어지고, mid 노드를 루트로 하는 서브 트리내 모든
            # 노드 색깔을 color로 변경해야 함.
        elif command == 300:
            m_id = data[1]
            # 이 경우 m_id는 현재 어떤 색인지 출력. 이미 주어진 노드 번호만 주어짐.
            cur_color = show_color(m_id, nodes)
            result.append(str(cur_color))
        elif command == 400:
            # 노드가 1개 이상인 경우에만 호출됨
            answer_worth = count_worth(roots, nodes)
            result.append(str(answer_worth))
            # 모든 노드의 가치를 계산하고, 가치 제곱의 합을 출력함.
    print("\n".join(result))

main()