# 자연수 n개를 만든다.
# 그 n개의 합은 s가 되어야 한다.
# 합이 s인 조합은 여러 개일 수 있다.
# 그중 곱이 가장 큰 조합을 찾아야 한다.
# 곱이 최대가 되려면 숫자들이 최대한 비슷해야 한다.
# 결과는 오름차순 배열로 return한다.
# 자연수 n개로 합 s를 만들 수 없으면 [-1]을 return한다.
from email.mime import base


def solution(n, s):
    # 5. 자연수 2개를 가지고는 합이 1인 집합을 만들 수 없으므로, -1이 들어있는 배열을 반환한다.
    if s < n:
        return [-1]

    # 1. 곱이 커지려면 최대한 똑같이 나눠주기
    # 최대한 공평하게 나눠주려면 최소 기본값을 알아야 한다.
    base = s // n

    # 2. 남은 수 구하기
    remainder = s % n

    # 3. 기본 배열 만들기
    result = [base] * n

    # 4. 남은 수만큼 뒤에서부터 1씩 더한다. 뒤에 값이 커진다. 그럼.
    for i in range(remainder):
        # n-1은 배열의 마지막 위치
        # i만큼 왼쪽으로 간 칸에 1을 더한다.
        result[n-1 - i] +=1
    # 답을 오름차순으로 return해야 하니까.
    return result

print(solution(2,9))
# [4, 5]

print(solution(2,1))
# [-1]

print(solution(2,8))
# [4,4]