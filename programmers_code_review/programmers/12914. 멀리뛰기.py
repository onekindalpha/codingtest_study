# n칸이 있을 때, 끝에 도달하는 방법
# 한번에 한칸 또는 2칸
# n % 1234567
# n칸에 가는 방법 = n-1칸에 가는 방법 + n-2칸에 가는 압법

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 3칸부터
    two_before = 1
    one_before = 2

    # 3칸 답부터 n칸 답까지 하나씩 만듦.
    for step in range(3, n  + 1):
        # 지금 계산해서 새로 만든 칸의 답
        current_answer = (two_before + one_before) % 1234567
        # 현재 칸을 계산하면, 자리를 바꿈.
        two_before = one_before
        one_before = current_answer

    return one_before

print(solution(4))
# 5

print(solution(3))
# 3