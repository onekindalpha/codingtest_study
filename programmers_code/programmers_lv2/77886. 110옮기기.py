# 0과 1로 이루어진 문자열 x에 대해 "110"을 뽑아서 임의의 위치에 다시 삽입
# s열에는 변형시킬 문자열 x가 여러 개 들어있음
# 각 문자열에 대해 위 행동으로 변형해서 만들 수 있는 문자열 중 사전 순으로 가장 앞에 오는 문자열을 배열에 담아 return
# 스택+그리디+문자열 처리

# 원본 문자열에는 110이 끝에 있지 않지만, stack을 쌓는순간에는 끝에 쌓일때 pop을 하기 때문에
# stack을 쓴느 것임.

# 사전순으로 최대한 앞에 오도록 x를 만들려면.. .음...
# "110"은 1로 시작한다.
# 그래서 남은 문자열 안에 0이 있으면,
# "110"을 그 0보다 앞에 두면 손해다.
# 따라서 남은 문자열의 마지막 0 뒤에 넣는다.
# 또한, 모든 0 뒤에는 1들만 남아있다면, 그 1들보다도 앞에 두는게 이득임.

def solution(s):
    answer = []
    # s에서 x를 하나씩 꺼낸다.
    for x in s:
        stack = []
        # 그안에서 연속된 110을 찾아서 뽑아낸 "110"의 개수
        count_110 = 0
        # 1. x에서 문자열을 하나씩 꺼내서 stack에 쌓는다.
        for char in x:
            stack.append(char)
            # 2. stack 끝 3글자가 "110"이면 뽑는다.
            if len(stack) >= 3 and stack[-3:] == ["1", "1", "0"]:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 +=1

        # 그리고 꺼낸다음에 빈 문자열을 붙여서 새 문자열을 만든다.
        # stack안의 문자열읠 중간에 아무것도 넣지 않고 붙인다는 의미에서 구분자 "" 를 사용함.
        remain = "".join(stack)
            # 그리고 남은 문자열에서 마지막 0을 찾는다.
        last_zero_index = remain.rfind("0")
        # 뽑아낸 "110"들을 만든다.
        out = "110" * count_110

                # 또한, 만약 모든 0 뒤에 1들만? 1들이 남아있다면
        # rfind는 못찾으면 -1을 줌
        if last_zero_index == -1:
                    # 그 1들보다는 앞에 위치시킨다.
            new_x = out + remain
                # 그렇지 않다면?
        else:
            #마지막 0 뒤에 "110"을 넣는다.
            new_x = (
                remain[:last_zero_index + 1]
                + out
                + remain[last_zero_index + 1:]
            )
    # 새 문자열을 answer에 넣는다.
        answer.append(new_x)
    return answer
print(solution(["1110", "100111100", "0111111010"]))
# 기대값: ["1101", "100110110", "0110110111"]


print(solution(["110"]))
# 기대값: ["110"]


print(solution(["1110"]))
# 기대값: ["1101"]

print(solution(["1110110"]))
# 기대값: ["1101101"]


print(solution(["1111"]))
# 기대값: ["1111"]


print(solution(["0000"]))
# 기대값: ["0000"]


print(solution(["110110"]))
# 기대값: ["110110"]


print(solution(["0110"]))
# 기대값: ["0110"]