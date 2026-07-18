# 야근 피로도
# 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값
# n시간동안 야근 피로도를 최소화하도록 일함
# 퇴근까지 남은 n시간과 각 일에 대한 작업량 works

import heapq

def solution(n, works):
    # n시간 안에 모든 일을 다 끝낼 수 있으면 피로도는 0
    if sum(works) <= n:
        return 0

    heap = []
    # 큰 작업량을 먼저 꺼내기 위해 음수로 넣는다.
    for work in works:
        heapq.heappush(heap, -work)

    # n시간 동안 반복한다.
    for _ in range(n):
        # 제일 큰 작업량을 꺼낸다.
        biggest_work = -heapq.heappop(heap)
        # 1시간 일했으니까 작업량을 1 줄인다.
        biggest_work -= 1
        # 다시 음수로 바꿔서 heap에 넣는다.
        heapq.heappush(heap, -biggest_work)

    answer = 0

    # heapq안에는 음수로 들어있지만,
    # 제곱하면 음수든 양수든 결과가 같다.
    for work in heap:
        answer += work * work

    return answer

print(solution(4, [4, 3, 3]))
# 12

print(solution(1, [2, 1, 2]))
# 6

print(solution(3, [1, 1]))
# 0