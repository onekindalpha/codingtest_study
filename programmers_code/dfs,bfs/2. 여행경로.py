# 방문순서가 중요함.
# [a, b] 인접리스트 배열? graph
# 2차월 배열 tickets, 방문하는 공항 경로를 배열에 담아 return 방문순서를 return하는 구나.
# 2. 시작은 ICN 공항에서 항상. start = "ICN"
# 알파벳 순서. 모든 공항은 알파벳 세글자.
# 모든 경로를 방문할 수 없는 경로는 주어지지 않습니다.
# 1. 주어진 항공권은 모두 사용해야 합니다. x2 (항공권=간선, 공항=노드, 모든 항공권 사용=모든 간선을 한번씩 사용)
# 보통 DFS에서는 방문한 노드는 다시 안가는데, 여긴 방문한 공항을 다시 갈 수 있음. 따라서, 항공권 사용 여부를 체크해야 함.
# DFS문제임.

def solution(tickets):
    # 알파벳 순이니까 항공권 정렬이 필요함.
    tickets.sort()
    # 방문기록표를 만듦.
    visited = [False] * len(tickets) # [False, False, False]
    # 시작하는 공항을 미리 넣어둠.
    path = ["ICN"]

    # 현재 공항에서 다음 항공권을 골라 여행 경로를 이어가는 함수를 만듦.
    # 핵심은 모든 항공권을 다 쓰는 것. path길이가 항공권 개수 +1 이면 모든 항공권을 다 쓴 것이므로 성공.
    def dfs(current):
        if len(path) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]
            # 아직 티켓을 안썼고, 출발지가 지금 내가 있는 공항이라면
            if not visited[i] and start == current:
                # 이번 티켓을 쓰는것으로 하자.
                visited[i] = True
                # 그 티켓이 도착 공항으로 이동했다는 의미.
                path.append(end)
                if dfs(end):
                    return True

                visited[i] = False
                path.pop()

        return False

    dfs("ICN")
    return path

print(solution(
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
))  # ["ICN", "JFK", "HND", "IAD"]

print(solution(
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
