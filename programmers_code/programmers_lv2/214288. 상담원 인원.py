# reqs = [a, b, c] -> c번 유형의 상담을 원하는 참가자가 a분에 b분 동안의 상담을 요청함. 오름차순 정렬.
# 멘토 n명, 1~k번으로 분류되는 상담 유형이 있음.
# 각 멘토는 k개의 상담 유형 중 하나만 담당 가능함.
# 멘토는 동시에 참가자 1명과만 상담 가능함, 상담시간은 참가자가 요청한 시간만큼 딱.
# 상담유형 담당 멘토 중 상담중이 아닌 멘토와 상담을 시작함

# 목적: 상담요청시부터 상담시작하기까지 기다린 시간의 합이 최소가 되도록 멘토인원을 정하려고 함.

import heapq
def solution(k, n, reqs):
    # 빈 리스트를 k+1개 만드려면
    requests_by_type = [[] for _ in range(k+1)]
    for a, b, c in reqs:
        #c번 유형요청을 requests_by_type[c]에 넣음.
        requests_by_type[c].append((a, b))

    def get_wait_time(requests, mentor_count):
        heap = [0] * mentor_count
        total_wait = 0
                # 이때, 대기자 리스트가 있다면, 먼저 상담 요청한 참가자가 우선됨
                # 우선순위 큐 사용함.
                # 큐에 넣을 것은 멘토별 다음 상담 가능 시각임.
        for a, b in requests:
            start_time = heapq.heappop(heap)
            if start_time <= a:
                wait = 0
                finish_time = a + b
            else:
                wait = start_time - a
                finish_time = start_time + b
            total_wait += wait
            heapq.heappush(heap, finish_time)
        return total_wait
    # 1) 상담유형별 멘토수별 총 대기시간을 만듦.
    # 멘토수를 그대로 인덱스로 쓰려고
    wait_table = [[0] * (n +1) for _ in range(k+1)]

    for type_num in range(1, k + 1):
        requests = requests_by_type[type_num]

        for mentor_count in range(1, n+1):
            # 몇번 유형에 몇번 멘토가 있을때, 대기시간.
            wait_table[type_num][mentor_count] = get_wait_time(requests,mentor_count)

    # 2) n명을 k개유형에 최소 1명씩 나누는 모든 경우를 DFS로 탐색
    answer = float("inf")
    def dfs(type_num, remaining, total_wait):
        nonlocal answer

        #k번 유형까지 다 배정한 경우.
        if type_num == k +1:
            if remaining == 0:
                answer = min(answer, total_wait)
            return
        #형까지 다 배정한 경우
        #현재 type_num유형에 줄 수 있는 멘토 수
        #뒤에 남은 유형들에게 최소 1명씩은 남겨야 함.
        remaining_type_count = k - type_num
        max_mentor_count = remaining - remaining_type_count
        #dfs를 수행한다.
        for mentor_count in range(1, max_mentor_count +1):
            dfs(type_num +1, remaining - mentor_count, total_wait + wait_table[type_num][mentor_count])
    #초기값 설정
    dfs(1, n, 0)
    return answer

# 테스트 1
k = 3
n = 5
reqs = [
    [10, 60, 1],
    [15, 100, 3],
    [20, 30, 1],
    [30, 50, 3],
    [50, 40, 1],
    [60, 30, 2],
    [65, 30, 1],
    [70, 100, 2]
]

print(solution(k, n, reqs))  # 25


# 테스트 2
k = 2
n = 3
reqs = [
    [5, 55, 2],
    [10, 90, 2],
    [20, 40, 2],
    [50, 45, 2],
    [100, 50, 2]
]

print(solution(k, n, reqs))  # 90
