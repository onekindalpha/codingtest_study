# 문제에서 요구하는 알고력과 코딩력보다 같거나 그 이상이어야 함.
# 둘중 하나라도 모자라면,
# 알고력 1을 높이기 위해서 1의 시간이 필요
# 코딩력 1을 높이기 위해서 1의 시간이 필요
# 현재 풀수있는 문제 중 하나를 풀어 알고력과 코딩력을 높임
# 각 문제마다 풀면 올라가는 알고력과 코딩력이 정해져 있음
# 문제 하나 푸는데 문제가 요구하는 시간이 필요하고, 같은 문제를 여러번 풀 수 있음
# 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간 구하기
from xml.sax.handler import all_properties

# 초기 알고력과 코딩력 alp, cop, 문제 정보 담은 배열 problems
# 모든 문제들을 풀 수 있는 알고력과 코딩력 얻는 최단시간 return
# 1. alp_req는 문제를 푸는데 필요한 알고력입니다.
# 2. cop_req는 문제를 푸는데 필요한 코딩력입니다.
# 3. alp_rwd는 문제를 풀었을 때 증가하는 알고력입니다.
# 4. cop_rwd는 문제를 풀었을 때 증가하는 코딩력입니다.
# 5. cost는 문제를 푸는데 드는 시간입니다.

# 목적: 공부/문제풀이를 통해 모든 문제를 풀 수 있는 능력치까지 도달하는 최소 시간을 구한다.
# DP는 최종 목적을 작은 목적들로 쪼갠 표
# # 능력치 상태를 순회하도록 함.
# 같은 능력치 상태에 여러 방법으로 도착할 수 있으니까,
# 각 상태마다 최소 시간만 저장해야 한다.
def solution(alp, cop, problems):
    # 1. 목표 능력치를 정하기
    target_alp = max(p[0] for p in problems)
    target_cop = max(p[1] for p in problems)

    #2. 시작점 보정. 이미 목표값 이상이면 그냥 목표값처럼 봄
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    #3. dp 표 만들기
    INF = float("inf")
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]

    #4. 처음에 주어진 alp, cop상태까지 도달하는데 걸린 추가 시간은 0
    dp[alp][cop] = 0

    # 현재 능력치에서
    for cur_alp in range(alp, target_alp + 1):
        for cur_cop in range(cop, target_cop + 1):

            # 알고력 공부
            if cur_alp < target_alp:
                dp[cur_alp + 1][cur_cop] = min(
                    dp[cur_alp + 1][cur_cop],
                    dp[cur_alp][cur_cop] + 1
                )

            # 코딩력 공부
            if cur_cop < target_cop:
                dp[cur_alp][cur_cop + 1] = min(
                    dp[cur_alp][cur_cop + 1],
                    dp[cur_alp][cur_cop] + 1
                )

            # 문제 풀이
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if cur_alp >= alp_req and cur_cop >= cop_req:
                    arrive_alp = min(target_alp, cur_alp + alp_rwd)
                    arrive_cop = min(target_cop, cur_cop + cop_rwd)

                    dp[arrive_alp][arrive_cop] = min(
                        dp[arrive_alp][arrive_cop],
                        dp[cur_alp][cur_cop] + cost
                    )

# 로 다음 상태를 갱신

    return dp[target_alp][target_cop]

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
# 15

print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
# 13