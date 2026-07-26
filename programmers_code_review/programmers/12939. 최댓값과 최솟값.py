
def solution(s):
    s = list(map(int, s.split()))
    new_s = []
    new_s.append(min(s))
    new_s.append(max(s))
    answer = " ".join(map(str, new_s))
    return answer


print(solution("1 2 3 4"))

print(solution("-1 -2 -3 -4"))

print(solution("-1 -1"))