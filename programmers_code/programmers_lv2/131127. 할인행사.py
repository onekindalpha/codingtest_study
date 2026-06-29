# want 정현이가 원하는 제품
# number 정현이가 원하는 제품의 수량
# discount XYZ 마트에서 할인하는 제품
# 연속된 10일동안 원하는 물건이 원하는 개수만큼있는지를 보면 되는가

from collections import Counter


def solution(want, number, discount):
    target = Counter()
    for i in range(len(want)):
        item = want[i]
        count = number[i]
        target[item] = count
    answer = 0
    # discount에서 10일짜리 구간을 하나씩 꺼내서 검사하기
    for start in range(len(discount)):
        ten_days = discount[start:start + 10]
        if len(ten_days) < 10:
            break
        ten_days_count = Counter(ten_days)
        if ten_days_count == target:
            answer += 1

    return answer

# 테스트 1: 프로그래머스 예시
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = [
    "chicken", "apple", "apple", "banana", "rice",
    "apple", "pork", "banana", "pork", "rice",
    "pot", "banana", "apple", "banana"
]

print(solution(want, number, discount))  # 3


# 테스트 2: 원하는 게 apple 10개인데 할인 목록에는 banana만 있음
want = ["apple"]
number = [10]
discount = [
    "banana", "banana", "banana", "banana", "banana",
    "banana", "banana", "banana", "banana", "banana"
]

print(solution(want, number, discount))  # 0
