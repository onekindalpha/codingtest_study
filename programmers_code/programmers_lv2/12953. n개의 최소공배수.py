# n개의 수의 최소공배수는 n개의 수들의 배수 중 공통이 되는 가장 작은 숫자
# n개의 숫자를 담은 배열 arr이 입력되었을때
# 이들의 최소공배수를 반환하는 함수
# 배열 최소공배수 = 앞에서부터 lcm을 누적한다.
import math
# 두수의 최소공배수를 구하는 함수를 작성
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)

    return answer

print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))      # 6
print(solution([12, 18, 24]))   # 72