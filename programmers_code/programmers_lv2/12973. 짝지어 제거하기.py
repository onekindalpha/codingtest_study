# 알파벳 소문자.
# 같은 알파벳이 두개 붙어있는 짝을 찾음
# 짝을 제거한뒤, 앞뒤로 문자열을 이어 붙임. -> 일단 앞 뒤로 분리해둔 상태에서
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기 종료됨
# 문자열 S가 주어졌을대, 성공적 반환함수 , 성공적 수행 return 1 아니면 0
# 같은 문자가 연속으로 붙으면 제거한다.
# 제거 후 앞뒤 문자가 다시 붙는다.
# 스택이 비어 있으면 넣는다.
# 스택 마지막 문자와 현재 문자가 같으면 pop 한다.
# 다르면 현재 문자를 push 한다.

def solution(s):
    stack = []
    for ch in s:
        # stack이 빈값이 아니고 마지막이랑 같으면
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    # not stack
    # not []
    # true
    return 1 if not stack else 0


print(solution("baabaa"))  # 1
print(solution("cdcd"))    # 0
print(solution("aa"))      # 1
print(solution("ab"))      # 0
print(solution("aabb"))    # 1
print(solution("abba"))    # 1
print(solution("abcddcba")) # 1
print(solution("abc"))     # 0
