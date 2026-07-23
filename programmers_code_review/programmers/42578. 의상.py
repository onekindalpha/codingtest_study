# 2차원 배열 clothes
# [의상의 이름, 의상의 종류]
# 의상 일부가 겹쳐도, 의상을 추가하거나 다른 의상이 겹치지 않으면 서로 다른 방법으로 옷을 착용한 것으로 계산함.
# 하루에 최소 한개는 입음
# 서로 다른 옷의 조합의 수 return
from collections import Counter

def solution(clothes):
    kind_count = Counter()
    # 종류별 개수를 센다
    for cloth in clothes:
        kind = cloth[1]
        kind_count[kind] += 1
    # 각 종류 개수에 1을 더한다
    answer = 1
    # 종류별 값을 전부 곱한다
    for count in kind_count.values():
        answer *= (count + 1)
    # 아무것도 안 입는 경우 1개를 뺀다
    answer -= 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# 5

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
# 3