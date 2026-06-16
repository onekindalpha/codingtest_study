def solution(n, computers):
    # 방문 여부를 기록하는 표
    visited = [False] * n
    answer = 0

    # computer가 속한 네트워크를 전부 방문 처리하는 함수
    def dfs(computer):
        visited[computer] = True

        for next_computer in range(n):
            # 현재 컴퓨터와 다음 컴퓨터가 연결되어 있고,
            # 다음 컴퓨터를 아직 방문하지 않았다면
            if computers[computer][next_computer] == 1 and not visited[next_computer]:
                dfs(next_computer)

    # 전체 컴퓨터를 돌면서 아직 방문 안 한 컴퓨터를 찾는다
    for computer in range(n):
        if not visited[computer]:
            # 아직 방문 안 한 컴퓨터를 만났다는 건 새 네트워크 발견
            answer += 1
            dfs(computer)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 2

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# 1