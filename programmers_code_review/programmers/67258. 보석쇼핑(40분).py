# 진열된 모든 종류 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
# gems는 진열대에 나열된 보석임
# gems원소는 알파벳 대문자임.
# 모든 보석을 하나이상 포함하는 가장 짧은 구간을 찾아서 return
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아 return
# 만약 가장 짧은 구간 여러개면 시작 진열대 번호가 가장 작은 구간을 return


def solution(gems):
    kind = len(set(gems))
    #투포인터 문제에서 구간은 리스트로 저장안하고 인덱스 2개로 표현함.
    # 현재 구간은 gems[left]부터 gems[right+1]까지로 표현하면 됨.
    # 알아야 할 것은 구간 안 보석 개수를 딕셔너리로 저장. 루비 몇개. 다ㅣ아 몇개.
    left = 0
    sentence_count ={}
    start = 0
    end = len(gems) -1

    for right in range(len(gems)):
        #right위치의 보석을 현재 구간에 1개 추가한다.
        gem = gems[right]
        if gem in sentence_count:
            sentence_count[gem] += 1
        else:
            sentence_count[gem] = 1

        #현재 구간 안에 모든 보석 종류가 있으면,
        while len(sentence_count) == kind:
            #현재 구간을 정답 후보로 본다.
            if right - left < end - start:
                start = left
                end = right
            # 왼쪽 보석  한개를 빼본다.
            left_gem = gems[left]
            sentence_count[left_gem] -= 1
            #0으로 남아있는건 지운다.
            if sentence_count[left_gem] == 0:
                del sentence_count[left_gem]
            left +=1
    return [start +1, end+1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [3, 7]

print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 3]

print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 1]

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# [1, 5]