# 이진법에서 십육진법까지 모든 진법
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
# 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열.
# # 단, 10~15는 각각 대문자 A~F로 출력한다.
# n진법: num = (몫 * n) + 나머지
def to_n(num, n):
    chars = "0123456789ABCDEF"
    #숫자 원본이 0이면 0으로 돌려준다.
    if num == 0:
        return "0"
    #n진법으로 바꾼 글자를 모아두는 문자열
    result = ""
    #숫자 원본이 0 보다 크면
    while num >0:
        result = chars[num % n] + result

        num //= n
    return result
def solution(n, t, m, p):
    nums = "" #말할 문자들을 이어붙인 문자열
    num = 0 #0부터 증가시킬 숫자

    while len(nums) < t * m:
        nums += to_n(num, n)
        num +=1
    answer = ''
    for i in range(t):
        answer += nums[(p - 1) + i * m]
    return answer

print(solution(2, 4, 2, 1))
# 0111

print(solution(16, 16, 2, 1))
# 02468ACE11111111

print(solution(16, 16, 2, 2))
# 13579BDF01234567