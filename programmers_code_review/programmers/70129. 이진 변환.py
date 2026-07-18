# 0과 1로 이루어진 어떤 문자열 x
# x의 모든 0을 제거함.
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿈
# S에는 1이 최소 하나이상 포함되어 있음

# 제거할 0의 개수
# 0 제거 후 길이
# 이진변환 결과

def solution(s):
    zero_count = 0
    change_count = 0
    while s != "1":
        #계속해서 이진 변환을 가한다.
        #첫째 0을 제거한다.
        zero_count += s.count("0")
        s = s.replace("0", "")
        #둘째, 2진법 문자열로 바꿈
        c = len(s)
        s = bin(c)[2:]
        #이진변환 회차
        change_count += 1

    return [change_count, zero_count]

print(solution("110010101001"))
# [3, 8]

print(solution("01110"))
# [3, 3]

print(solution("1111111"))
# [4, 1]