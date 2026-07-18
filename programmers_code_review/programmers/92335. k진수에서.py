# 양의 정수 n
# k진수로 바꿨을 때, 조건에 맞는 소수가 몇개인지
# 1. 소수 양쪽에 0
# 2. 소수 오른쪽에 0, 왼쪽에는 아무것도 없음
# 3. 소수 왼쪽에 0, 오른쪽에 아무것도 없음
# 4. 소수 양쪽에 아무것도 없음
# 5. P는 각 자릿수에 0을 포함하지 않는 소수임
# 10진법으로 보았을때 소수.
# n, k가 매개변수로 주어짐.

# 참고로 1은 소수가 아님.

# 일단 n을 k진수로 바꿔야 함.
# converted = 로 저장
# 각가의 진수에서
# converted된 것에 , 5가지 조건에 맞는 소수가 몇개 들어있는지.
# 0을 기준으로 짤랐을때, 나오는 숫자 조각 P를 검사해서 소수인 것만 세면 됨.
# P = converted.split("0")
# P가 소수인지 확인을 하고,
# 그 개수를 리턴하면 됨.

# 1. n을 k진수 문자열로 바꾸는 함수
# n = (몫 * k) + 나머지
# n을 k로 나눈 나머지 = k진수의 맨 뒤 자리
# n을 k로 나눈 몫으로 갱신
# n이 0이 될 때까지 반복
# 마지막에 뒤집기

def convert_n_to_k(n, k):
    converted = []
    while n>0:
        converted.append(str(n % k))
        n //= k
    return ''.join(reversed(converted))


# 3. 나온 조각을 10진수 숫자로 보고 소수인지 검사하는 함수.
def is_prime(num):
    #1은 소수가 될 수 없음
    if num <2:
        return False
    # 소수의 조건은 1과 자기 자신 말고는 나누어 떨어지는 수가 없어야 함.
    # √num. 약수는 짝으로 나오기 때문.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 2. 그 문자열을 0 기준으로 짤라서 P에 리스트로 저장함.
def solution(n, k):
    converted = convert_n_to_k(n, k)
    P = converted.split("0")

    answer = 0
    for p in P:
        if p == "":
            continue

        num = int(p)

        if is_prime(num):
            answer += 1

    return answer

print(solution(437674, 3))   # 3
print(solution(110011, 10))  # 2