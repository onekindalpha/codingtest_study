# #동전조합개수 dp
# 금액 n을 만드는 경우의 수
# 동전을 여러 번 사용할 수 있음
# 이전 금액의 경우의 수로 현재 금액을 갱신함

def solution(n, money):
    MOD = 1000000007

    #dp[i]는 i원을 만드는 방법의 수.
    #동전을 하나씩 고정하고, coin부터 n까지 누적 갱신한다.
    dp = [0] * (n + 1)
    #0원을 만드는 방법은 1가지. 아무 동전도 안씀
    dp[0] = 1
    # 동전을 하나씩 꺼내보면서, 이전금액을 만드는 방법 뒤에 현재 금액을 붙인다.
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price - coin]
            dp[price] %= MOD

    return dp[n]

print(solution(6, [2, 3]))  # 2
print(solution(5, [2, 3]))  # 1
print(solution(4, [2, 3]))  # 1
print(solution(7, [2, 3]))  # 1