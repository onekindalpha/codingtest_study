# 짝궁이 있는 지를 봐야함. 근ㄷ네 순서는 ()이어야 함. (())도 상관없고, ((()))도 상관없음.
# 필: 마지막에 )로 닫혀야 하고. 또, 전체 수는 짝수여야 함.
# 올바른 괄호이면 true, 올바르지 않은 괄호면 false
# 왼쪽부터 처리하면서 현재 열려있는 괄호 개수를 추적

def solution(s):
    # 스택에는 문자를 넣음.
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        elif s[i] == ")":
            # 닫을 "("가 없으면 실패
            if stack == []:
                return False
            # 닫을 "("가 있으면 하나 꺼낸다
            stack.pop()

    if stack == []:
        return True
    else:
        return False