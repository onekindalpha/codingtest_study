# 선수의 수 n. a의 실력이 좋으면 b선수를 항상 이김.
# 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없음.
# 경기 결과 2차원 배열 results
# n은 1이상 100명 이하, results는 1개 이상 4,500개 이하.
# results 배열 각 행 [A, B]는 A선수가 B선수를 이겼다는 의미입니다.
# 모든 경기 결과에는 모순이 없습니다.
# 정확하게 순위를 매길 수 있는 선수의 수를 return이 무슨 의미지?
# 나보다 강한 사람 수 + 나보다 약한 사람 수 = n-1. 간접승패깢.

def solution(n, results):
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)

    def count_players(start, graph):
        # 선수를 이미 toT는지 기록하는 배열이다.
        visited = [False] * (n+1)
        # current 선수에서 출발해 갈 수 있는 선수 수를 센다.
        # current 기준으로 새로 발견한 선수 수를 count라고 한다.
        def dfs(current):
            count = 0
            # current와 연결된 다음 선수들을 확인한다.
            for next_player in graph[current]:
                # 아직 세지 않은 선수라면
                if not visited[next_player]:
                    # 이제 방문처리
                    visited[next_player] = True
                    # 새 선수 1명을 발견했으므로 +1
                    count +=1
                    # 그 선수가 또 이길/질 수 있는 선수들도 이어서 센다.
                    count += dfs(next_player)
            # current에서 도달 가능한 총 선수 수 반환
            return count
        # 시작 선수 자기 자신은 세면 안 되므로 미리 방문 처리
        visited[start] = True
        # start에서 출발해 도달 가능한 선수 수 반환
        return dfs(start)

    answer = 0

    for player in range(1, n+1):
        win_count = count_players(player, win_graph)
        lose_count = count_players(player, lose_graph)

        if win_count + lose_count == n -1 :
            answer += 1
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]] ))
#2