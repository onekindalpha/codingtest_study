# 이 문명이 사용하던 진법 체계는 10진법이 아니며, 2 ~ 9진법 중 하나이다.
# X로 표시된 부분이 지워진 결괏값이다.
# 이미 결괏값이 적힌 수식을 보고 이 문명이 사용하던 진법을 추론한다.
# 결괏값이 불확실한 수식은 ?를 사용한다.
# 가능한 진법들에서 결괏값이 모두 같으면 그 값으로 X를 채운다.
# 결괏값이 지워진 수식들의 결괏값을 채워 넣어 순서대로 문자열 배열에 담아 return한다.

def is_valid_number(number, base):
    # number가 문자열로 들어오기 때문에
    for digit in number:
        if int(digit) >= base:
            return False
    return True
# 진법 숫자를 10진수 숫자로 바꾸는 함수
def to_decimal(number, base):
    # 지금까지 읽은 숫자를 10진수로 바꿔서 저장해둔 값
    current_value = 0

    for digit in number:
        current_value = current_value * base + int(digit)

    return current_value
# 10진수 number을 base진법 문자열로 바꾼다.
def from_decimal(number, base):
    if number == 0:
        return "0"

    result = ""

    while number > 0:
        digit = number % base
        result = str(digit) + result
        number = number // base

    return result

def solution(expressions):
    # 가능한 진법만 모으기
    possible_bases = []
    for base in range(2, 10):
        possible = True

        for expression in expressions:
            left_number, operator, right_number, equal_sign, result = expression.split()

            if not is_valid_number(left_number, base):
                possible = False
                break
            if not is_valid_number(right_number, base):
                possible = False
                break
            if result != "X" and not is_valid_number(result, base):
                possible = False
                break
            if result == "X":
                continue

            left_value = to_decimal(left_number, base)
            right_value = to_decimal(right_number, base)
            result_value = to_decimal(result, base)

            if operator == "+":
                calculated_value = left_value + right_value
            else:
                calculated_value = left_value - right_value

            if calculated_value != result_value:
                possible = False
                break
        if possible:
            possible_bases.append(base)

    answer = []

    for expression in expressions:
        left_number, operator, right_number, equal_sign, result = expression.split()

        if result != "X":
            continue

        possible_results = set()

        for base in possible_bases:
            left_value = to_decimal(left_number, base)
            right_value = to_decimal(right_number, base)

            if operator == "+":
                calculated_value = left_value + right_value
            else:
                calculated_value = left_value - right_value
            calculated_result = from_decimal(calculated_value, base)
            possible_results.add(calculated_result)

        if len(possible_results) == 1:
            final_result = possible_results.pop()
        else:
            final_result = "?"
        answer.append(left_number + " " + operator + " " + right_number + " = " + final_result)
    return answer

# =========================
# 테스트 코드
# =========================

print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
# ["13 - 6 = 5"]

print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# ["1 + 5 = ?", "1 + 2 = 3"]

print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]

print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
# ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]

print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
# ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]
