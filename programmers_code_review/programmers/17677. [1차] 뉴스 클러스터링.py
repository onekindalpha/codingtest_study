# 교집합개수 / 합집합수
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한
# 교집합과 합집합이 바로 계산되는 것 -> 딕셔너리와 카운터
from collections import Counter


def make_pairs(s):
    s = s.lower()
    results = []
    # 페어를 만들 횟수 = 페어 시작점 개수만큼 반복
    for i in range(len(s) -1):
        pair = s[i:i+2]
    # 숫자 공백, 특수문자 거르기 -> .isalpha()
        # 한글 거르기 -> .isascii()
        if pair.isalpha() and pair.isascii():
            results.append(pair)
    return results

def solution(str1, str2):
    str1_list = make_pairs(str1)
    str2_list = make_pairs(str2)
    #교집합 합집합은 카운터 사용이 편리함
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    #같은 조각은 적게 나온 개수만큼 교집합
    intersection = counter1 & counter2
    #전체 조각은 많이 나온 개수만큼 합집합
    union = counter1 | counter2
    # 교집합과 합집합의 각각 개수를 구한다.
    intersection_count = sum(intersection.values())  # 2
    union_count = sum(union.values())  # 4
    #합집합이 0이면,자카도 유사도는 1이 되도록 65536을 리턴한다.
    if union_count == 0:
        return 65536
    return int(intersection_count / union_count * 65536)

print(solution("FRANCE", "french"))
# 16384

print(solution("handshake", "shake hands"))
# 65536

print(solution("aa1+aa2", "AAAA12"))
# 43690

print(solution("E=M*C^2", "e=m*c^2"))
# 65536