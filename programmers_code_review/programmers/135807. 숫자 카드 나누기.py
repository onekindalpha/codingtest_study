from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    #원소크기가 엄청 큰데? 배열의 길이도 길고
    #두 배열에는 중복된 원소가 있을 수 있다고 함.
    # 철수 가진 카드들을 모두 나눌 수 있는 양의 정수가 하나 있거나
    # 모두 나눌 수 있는 약수 = 공약수. 최대공약수
    chulsoo= reduce(gcd, arrayA)
    younghee = reduce(gcd, arrayB)
    # 영희 의 경우도
    # 아근데 다른 배열의 원소 하나라도 나눌 수 있으면 안되.ㅁ
    answer = 0
    # chulsoo가 arrayA는 모두 나눌 수 있는 건 이미 gcd로 보장됨
    # 이제 arrayB를 하나도 나눌 수 없는지만 확인하면 됨
    if all(num % chulsoo !=0 for num in arrayB):
        answer = max(answer, chulsoo)
    # younghee가 arrayB는 모두 나눌 수 있는 건 이미 gcd로 보장됨
    # 이제 arrayA를 하나도 나눌 수 없는지만 확인하면 됨
    if all (num % younghee !=0 for num in arrayA):
       answer = max(answer, younghee)

    return answer


print(solution([10, 17], [5, 20]))              # 0
print(solution([10, 20], [5, 17]))              # 10
print(solution([14, 35, 119], [18, 30, 102]))   # 7

print(solution([6, 12, 18], [5, 10, 25]))       # 6
print(solution([5, 10, 15], [12, 24, 36]))      # 12
print(solution([4, 8, 12], [8, 16, 24]))        # 0
print(solution([4, 4, 4], [3, 6, 9]))           # 4
print(solution([7], [14]))                      # 14
print(solution([7], [7]))                       # 0
print(solution([6, 10, 15], [7, 11, 13]))       # 0