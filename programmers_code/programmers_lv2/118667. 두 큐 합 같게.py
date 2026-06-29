# 두 큐의 원소 합이 같아져야 함.

from collections import Counter, deque

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    # 나머지가 1이면 안됨.
    if total % 2 == 1:
        return -1
    # 목표 합은 total //2 의 몫.
    target = total //2
    current_sum = sum(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    count = 0
    limit = len(queue1) *3
    while count <= limit:
        if current_sum == target:
            return count
        if current_sum > target:
            x = q1.popleft()
            current_sum -=x
            q2.append(x)
        else:
            x = q2.popleft()
            current_sum += x
            q1.append(x)
        count += 1

    return -1

# 테스트 코드
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5]))              # -1
print(solution([1, 1], [1, 1]))              # 0
print(solution([1, 2], [3, 4]))              # -1