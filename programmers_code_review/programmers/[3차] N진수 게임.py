# 입력
# n = 진법
# t = 튜브가 말할 글자 수
# m = 참가자 수
# p = 튜브 순서

# 게임 규칙
# 숫자는 0부터 시작한다.
# 숫자는 n진법 문자열로 바꿔서 말한다.
# 숫자 문자열 길이가 2 이상이면 한 글자씩 나눠서 말한다.
# 10~15는 A~F로 표현한다.

# n진법
# n진법 = 한 자리에서 0부터 n-1까지 사용한다.
# n-1 다음 숫자는 자리올림으로 표현한다.
# 2진법: 0, 1, 10, 11, 100, 101, 110, 111 ...
# 3진법: 0, 1, 2, 10, 11, 12, 20, 21, 22, 100 ...
# 16진법: 0, 1, 2, ..., 9, A, B, C, D, E, F, 10 ...

# 진법 변환 원리
# 10진수 x를 n으로 나눈 나머지는 n진수의 오른쪽 자리부터 나온다.
# 나머지를 문자로 바꿔 result 앞에 붙인다.
# x를 n으로 나눈 몫으로 줄인다.
# x가 0이 되면 변환을 끝낸다.
def convert(x, n):
    # 나머지를 문자로 바꾸는 표
    digits = "0123456789ABCDEF"

    # 0은 모든 진법에서 "0"
    if x == 0:
        return "0"

    # n진수 변환 결과
    result = ""

    # x가 0이 될 때까지 n으로 나눈다.
    while x > 0:
        # n으로 나눈 나머지
        remainder = x % n

        # 나머지를 문자로 바꿔 앞에 붙인다.
        result = digits[remainder] + result

        # x를 몫으로 갱신한다.
        x //= n

    return result


def solution(n, t, m, p):
    # 참가자들이 말하는 전체 문자열
    game = ""

    # n진수로 변환할 10진수
    current_number = 0

    # 튜브가 t글자를 뽑을 수 있는 길이까지 game을 만든다.
    while len(game) < t * m:
        # current_number를 n진수 문자열로 바꿔 game 뒤에 붙인다.
        game += convert(current_number, n)

        # 다음 10진수로 이동한다.
        current_number += 1

    # 튜브가 말할 문자열
    answer = ""

    # 튜브의 첫 번째 차례 인덱스
    # p는 1부터 시작하고, 문자열 인덱스는 0부터 시작한다.
    index = p - 1

    # 튜브가 t글자를 말할 때까지 반복한다.
    while len(answer) < t:
        # 튜브 차례의 문자를 answer에 붙인다.
        answer += game[index]

        # 다음 튜브 차례로 이동한다.
        # 참가자 수가 m명이므로 튜브 차례는 m칸 뒤에 온다.
        index += m

    return answer

# 출력
# 튜브가 말하는 t글자를 공백 없이 이어 붙인 문자열