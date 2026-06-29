def convert_to_k_base(n, k):
    result = ""

    while n > 0:
        result = str(n % k) + result
        n //= k

    return result


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def solution(n, k):
    converted_number = convert_to_k_base(n, k)

    candidates = converted_number.split("0")

    answer = 0

    for candidate in candidates:
        if candidate == "":
            continue

        number = int(candidate)

        if is_prime(number):
            answer += 1

    return answer

print(solution(437674, 3))    # 3
print(solution(110011, 10))   # 2