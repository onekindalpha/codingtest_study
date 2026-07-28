# 소수는 1보다 큰 자연수 중에서 약수가 1과 자기자신뿐인 수
# 약수는 어떤 수를 나누었을때 나머지가 0이 되는 수
# 2부터 자기 자신 전까지 나누어떨어지는 수가 있는지 봄
# for문을 여러번 돌릴 수가 없어서 파이썬이 순열을 만들어주는 함수를 사용함. permutations
from itertools import permutations
# 만들어진 숫자가 소수인지 판별하는 함수.
def is_prime(num):
    if num < 2:
        return False
    #오래걸림 방지. 소수 검사 시 num-1까지 안보고 제곱근까지만 볼 것.
    # 소수검사에서 약수를 찾을 때는 2부터 제곱근까지만 보면 됨.
    # 제곱근보다 큰 약수는 이미 작은 짝 약수에서 걸림
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    nums = set()
    ## ① 만들 숫자의 길이를 1부터 numbers 전체 길이까지 바꾼다.
    for length in range(1, len(numbers) + 1):
        # # # ② numbers에서 length(자리)개를 뽑아 순서 있게 나열한 경우를 하나씩 꺼낸다.
        # 꺼내서 그 하나를 perm이라는 튜플 변수에 담고, 아래 코드를 실행한다.
        for perm in permutations(numbers, length):
            ## # ③ 튜플 perm을 문자열로 합치고, int로 바꿔 숫자로 만든다.
            #011과 11은 같아짐.
            num = int("".join(perm))
            #중복제거도 됨.
            nums.add(num)
    answer = 0
    for num in nums:
        if is_prime(num):
            answer +=1
    return answer

print(solution("17"))
print(solution("011"))