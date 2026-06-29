# 1이 될때까지 이진변환을 가함

# return [변환 횟수, 제거한 0의 총개수]

def solution(s):
    transform_count = 0
    zero_total = 0

    while s != "1":
        zero_count = s.count("0")
        zero_total += zero_count
        one_count = len(s) - zero_count
        s = bin(one_count)[2:]
        transform_count += 1

    return [transform_count, zero_total]

# 테스트 코드
print(solution("110010101001"))  # [3, 8]
print(solution("01110"))         # [3, 3]
print(solution("1111111"))       # [4, 1]
print(solution("110"))           # [2, 2]
print(solution("10"))            # [1, 1]
print(solution("1"))             # [0, 0]