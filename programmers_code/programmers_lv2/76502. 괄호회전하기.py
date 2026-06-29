# text는 검사할 괄호 문자열로, 예를 들어서 "([])"
def is_correct(text):
    stack = []
    for ch in text:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
            #단는 괄호를 만났는데 스택이 이미 비어있으면.
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if ch == ")" and last_open != "(":
                return False
            if ch == "]" and last_open != "[":
                return False
            if ch == "}" and last_open != "{":
                return False
    return len(stack) == 0

def solution(s):
    answer = 0
    for cut in range(len(s)):
        related = s[cut:] + s[:cut]

        if is_correct(related):
            answer += 1
    return answer

# 테스트 코드
print(solution("[](){}"))   # 3
print(solution("}]()[{"))   # 2
print(solution("[)(]"))     # 0
print(solution("}}}"))      # 0