#한번에 k칸 앞으로 점프, (현재까지 온 거리)x2에 해당하는 위치로 순간이동 가능
# 순간이동 말고 점프 시 건전지 사용량이 듦.
# 거리가 n만큼 떨어져 있는 장소
# 건전지 사용량 최소

# n이 짝수면: 순간이동으로 온 거니까 2로 나눈다. 배터리 사용 없음.
# n이 홀수면: 순간이동으로 바로 올 수 없음. 1칸 점프가 필요했던 거니까 배터리 +1. n에서 1을 뺀다.

def solution(n):
    battery = 0

    while n>0:
        if n % 2 == 0:
            n = n//2
        else:
            battery += 1
            n -= 1
    return battery

print(solution(5))     # 2
print(solution(6))     # 2
print(solution(5000))  # 5