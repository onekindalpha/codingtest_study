# 최소 필요도와 소모 필요도
# 던전은 한 번만 탐험할 수 있다.
# 현재 피로도 k, 던전별 "최소 필요 피로도"와 "소모 필로도"가 담긴 2차원 배열 dungeons가 매개변수로 주어질 때, 유저가 탐험할 수 있는 최대 던전 수를 return
# k는 5000이하,
# dungeons의 세로 행 길이는 1이상 8이하, dungeons의 각 행은 ["최소 필요 피로도", "소모 피로도"]이며, 전자가 후자보다 항상 크거나 같고, 둘다 1000이하인 자연수임.
# 서로 다른 던전의 경우 ["최소 필요 피로도", "소모 피로도"] 세트는 같을 수 있음.
# 던전을 어떤 순서로 방문해야 가장 많이 돌 수 있는가?

# 핵심: 현재 피로도로 갈 수 있는 던전을 찾아 본다.
def solution(k, dungeons):
    # 가장 많이 돈 던전 개수
    answer = 0
    # 갈 수 있으면 들어간다.
    # 던전 방문 여부
    visited  = [False] * len(dungeons)

    # 현재 피로도와 방문한 던전 수를 기준으로, 갈 수 있는 던전 순서를 탐색한다.
    def dfs(current_fatigue, count):
        # 바깥쪽에 있는 answer를 스고 바꾸겠다.
        nonlocal answer
        # 지금 count가 최고 기록보다 크면 answer를 바꾼다.
        answer = max(answer, count)

    # 던전 개수를 하나씩 늘려나감.
        for i in range(len(dungeons)):
            # 최소 필요 피로도, 소모 필요도
            need, cost = dungeons[i]
            if not visited[i] and current_fatigue >= need:
                visited[i] = True
                # 피로도 깎고, 던전 하나 돌았으니 count 하나 추가함
                dfs(current_fatigue-cost, count + 1)
            #다른 순서도 보기 위해 방문을 취소한다. => 이 부분이 백트래킹
                visited[i] = False

    #그 상태로 다음 던전을 또 찾아본다.
    # 처음 피로도 k로 시작. 아직 돈 던전은 0개.
    dfs(k, 0)
    # 다 보고 나면 방문 표시를 지우고 다른 순서도 시도한다.
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))
#3


# 시간 복잡도는 O(N!)  ex. N × (N-1) × (N-2) × ... × 1 = N!
# 공간 복잡도는 O(N)
