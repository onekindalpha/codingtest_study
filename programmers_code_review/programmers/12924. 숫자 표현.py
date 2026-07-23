# 연속된 자연수들로 n을 표현하는 방법의 수
# 투 포인터(슬라이딩 윈도우) 또는 수학적 약수 성질로 풀기

def solution(n):
    answer = 0
    for start in range(1, n+1):
        total = 0

        for num in range(start, n+1):
            total += num

            if total == n:
                answer += 1
                break
            if total > n:
                break
    return answer

print(solution(15))