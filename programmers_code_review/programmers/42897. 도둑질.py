# 모든 집은 동그랗게 배치되어있다.
# 인접한 두 집을 털면 경보가 울림. -> 인접한 집은 털면 안됨.
# 각 집에 있는 돈이 담긴 배열 money가 주어질때, 도둑이 훔칠 수 있는 돈의 최댓값
# 마을에 있는 집은 3개 이상 1,000,000개 이하임.
# 인접한 것을 고르면 안되는 최댓값 dp문제
# 번외: 최댓값/최솟값을 구ㅐㅎ야 한다. + 앞에서 고른 선택이 뒤 선택에 영향을 준다 + 모든 경우를 다 보면 너무 많다. + 작은 문제의 답을 저장해서 다음 문제에 쓸 수 있다. -> dp의심

def solution(money):
    def steal_line(money):
        house_count = len(money)

        # dp라는 메모장을 실제로 만들기.  (ex. dp = [0, 0, 0, 0])
        dp = [0] * house_count
        dp[0] = money[0]
        dp[1] = max(money[0], money[1])

        # 리스크 : 바로 현재 집을 털면 바로 전 집을 못 턴다.
        # 현재 집을 터는 경우 = 두 칸 전까지의 최댓값 + 현재 집 돈
        # 현재 집을 안 터는 경우 = 한 칸 전 까지의 최댓값
        # 둘중에 큰 값을 고르면 된다.
        # 그 다음에는 반복문으로 간다.
        for i in range(2, house_count):
            dp[i] = max(dp[i-1], dp[i-2]+ money[i])
        return dp[house_count -1]

    case_without_last_house = steal_line(money[:-1])
    case_without_first_house = steal_line(money[1:])

    return max(case_without_last_house, case_without_first_house)

print(solution([1,2,3,1]))
#4

#
# dp[0], dp[1]을 무조건 설정하는 게 아니다.
#
# 내 공식이 dp[i - 1], dp[i - 2]를 쓰면
# dp[0], dp[1]이 필요하다.
#
# 내 공식이 dp[i - 1]만 쓰면
# dp[0]만 필요할 수도 있다.
#
# 2차원 DP면 첫 줄, 첫 칸이 초기값이 될 수도 있다.