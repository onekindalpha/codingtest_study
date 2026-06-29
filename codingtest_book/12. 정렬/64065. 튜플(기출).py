
def solution(s):
    answer = []
    s = s[2:-2]

    groups =s.split("},{")

    groups.sort(key=len)

    for group in groups:
        numbers = group.split(",")

        for number in numbers:
            number = int(number)

            if number not in answer:
                answer.append(number)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# [2, 1, 3, 4]

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# [2, 1, 3, 4]

print(solution("{{20,111},{111}}"))
# [111, 20]

print(solution("{{123}}"))
# [123]

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# [3, 2, 4, 1]