# 왼쪽 토핑 종류 수와 오른쪽 토핑 종류 수가 같도록 짤라야 함
# 토핑개수가 아니라 토핑종류.
# 자를 수 있는 모든 위치를 본다.
# 하나씩 왼쪽으로 옮긴다.
# left_set = {}
# # 왼쪽에 하나씩
# left_set.add(t)
# # 왼쪽의 종류 수
# len(left_set)
# 오른쪽
from collections import Counter

def solution(topping):
    answer = 0

    left_set = set()
    right_counter = Counter(topping)

    for t in topping[:-1]:
        left_set.add(t)

        right_counter[t] -=1

        # 없는 토핑이 되면, 오른쪽 종류 목록에서 t를 지운다.
        if right_counter[t] == 0:
            del right_counter[t]

        # 왼쪽과 오른쪽의 토핑 종류 수를 비교한다.
        if len(left_set) == len(right_counter):
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
print(solution([1, 2, 3, 1, 4]))           # 0
print(solution([1, 1, 1, 1]))              # 3
print(solution([1, 2]))                    # 1
