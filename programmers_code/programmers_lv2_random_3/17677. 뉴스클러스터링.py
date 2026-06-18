# 문자열 + 다중집합 + counter문제 -> 문자열을 잘라서 개수를 세는 문제.
# 자카드 유사도 공식 = 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# 교집합은 min(개수), 합집합은 max(개수)
# 문자열은 두 글자씩 끊어서 다중집합의 원소로 만듦.
# 영문자로 된 글자 상만 유효하고, 기타 공백이나 숫자, 특수문자가 들어있는 경우는 버린다.
# 집합 A와 집합 B가 모두 공집합일 경우에는 자카드 유사도를 1로 정의한다
# 문자열 두개를 받는다.
# 각 문자열을 두 글자씩 자른다.
# 마지막 한글자만 남은 위치는 볼 수 없음.
# ex. s = "ABCD" -> len(s)-1개가 두글자 쌍을 만들 수 있음
# 카운터는 리스트 안에 같은 값이 몇 번 나왔는지 자동으로 세어주는 도구임. 같은거 몇번 나왔는지.
from collections import Counter
# 두글자 쌍 만드는 함수
def solution(str1, str2):
    def make_pairs(s):
        s = s.lower()
        results = []

        for i in range(len(s) - 1):
            pair = s[i:i+2]

            # 영어 두 글자인 것만 남긴다. isalpha() 파이썬 문자열 내장 매서드.
            if pair.isalpha() and pair.isascii():
                results.append(pair)
        return results
# 각 조각이 몇번 나왔는지 센다.

    list1 = make_pairs(str1)
    list2 = make_pairs(str2)

    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # 같은 조각은 적게 나온 개수만큼 교집합.
    intersection = counter1 & counter2
    # 전체 조각은 많이 나온 개수만큼 합집합
    union = counter1 | counter2

    # Counter 안의 개수들을 모두 더한다.
    intersection_count = sum(intersection.values())
    union_count = sum(union.values())

    # 둘 다 공집합이면 자카드 유사도는 1
    if union_count == 0:
        return 65536
    # 교집합 / 합집합 * 65536을 한다.
    return int(intersection_count / union_count * 65536)

print(solution("FRANCE", "french"))
# 16384

print(solution("handshake", "shake hands"))
# 65536

print(solution("aa1+aa2", "AAAA12"))
# 43690

print(solution("E=M*C^2", "e=m*c^2"))
# 65536