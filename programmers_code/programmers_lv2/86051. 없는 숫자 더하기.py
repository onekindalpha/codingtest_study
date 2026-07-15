# numbers는 0에서 9까지의 숫자 중ㅇ 일부임
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
# 차집합 / 전체합 - 부분합

def solution(numbers):
    answer = 0
    for num in range(10):
        if num not in numbers:
            answer += num

    return answer

print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
# 기대값: 14
# 없는 숫자: 5, 9


print(solution([5, 8, 4, 0, 6, 7, 9]))
# 기대값: 6
# 없는 숫자: 1, 2, 3


print(solution([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 기대값: 0
# 없는 숫자 없음


print(solution([0]))
# 기대값: 45
# 없는 숫자: 1~9


print(solution([9]))
# 기대값: 36
# 없는 숫자: 0~8


print(solution([1, 3, 5, 7, 9]))
# 기대값: 20
# 없는 숫자: 0, 2, 4, 6, 8