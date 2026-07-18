# 하나의 트리 형태로 연결. n개의 송전탑. 전선중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다.
# 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞춤.
# 송전탑의 개수 n, 전선 정보 wires, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)을 return
# n 2이상 100이하. wires는 n-1인 2차원 배열 ! n+1까지 해야힘
# wires = [v1, v2], 1 <= v1 < v2 <= n

# 한쪽 개수 세면 나머지는 n-count.
# 양방향
def solution(n, wires):
    #wires = sorted(wires)
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    #무작정 끊어보기 - 끊었다고 생각. 막혔다고 생각하고 dfs수행
    def count_tower(start, cut_v1, cut_v2):
        visited = [False] * (n+1)
        stack = [start]
        visited[start] = True
        # 전선 하나를 끊었을대, 한쪽 전력망에 송전탑이 몇 개 있는지 셈.
        count = 0

        # 반복문 stack (내가 stack을 관리함 -탐색과정을 통제하고 싶을때. 재귀는 하나로 깊이 파고들때. )
        while stack:
            current = stack.pop()
            count += 1
            for next_node in graph[current]:
                if (current == cut_v1 and next_node == cut_v2) or (current == cut_v2 and next_node == cut_v1):
                    continue
                if not visited[next_node]:
                    visited[next_node] =  True
                    stack.append(next_node)
        return count

    answer = n

    for cut_v1, cut_v2 in wires:
        # cut_v1에서 출발해서, cut_v1- cut_v2 전선은 끊긴 척하고, 갈 수 있는 송전탑 개수를 셈.
        count = count_tower(cut_v1, cut_v1, cut_v2)
        other = n - count
        # 두 전력망 개수의 차이
        diff = abs(count-other)
        # 이번에 구한 차이와 위에서 answer을 비교한다.
        answer = min(answer, diff)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# 3
print(solution(4,[[1,2],[2,3],[3,4]]))
# 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# 1