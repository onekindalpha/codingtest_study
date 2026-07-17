# 길이가 같은 두개의 큐
# 하나의 큐를 골라 pop, 다른 큐에 insert 해서
# 각 큐의 원소 합이 같도록
# 할때 작업의 최소 횟수
# pop + insert까지 1회 수행 카운트
# 어떠한 경우로도 원소 합 같게 못 만들면 -1을 리턴

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    queue1_sum = sum(q1)
    queue2_sum = sum(q2)
    total_sum = queue1_sum + queue2_sum

    if total_sum % 2 == 1:
        return -1

    target_sum = total_sum // 2
    count = 0
    limit = (len(queue1) + len(queue2)) * 2

    while count <= limit:
        if queue1_sum == target_sum:
            return count

        if queue1_sum > target_sum:
            num = q1.popleft()
            q2.append(num)
            queue1_sum -= num
            queue2_sum += num
        else:
            num = q2.popleft()
            q1.append(num)
            queue2_sum -= num
            queue1_sum += num

        count += 1

    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5]))              # -1