# 가로 2, 세로 1
# 바닥 가로 n, 세로 2을 채우려고 함.
# 타일을 가로로 배치, 타일을 세로로 배치
# 패턴을 보면

def solution(n):
    MOD = 1000000007
    # 초기값 처리
    if n ==1:
        return 1

    # 답을 지정할 칸
    ways = [0] * (n+1)

    ways[1] = 1
    ways[2] = 2

    for i in range(3, n+1):
        ways[i] = (ways[i-2] + ways[i-1]) % MOD

    return ways[n]

print(solution(4))
# 5

