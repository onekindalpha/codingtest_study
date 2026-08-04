import heapq

def solution(n, k, enemy):
    heap = []
    for i, e in enumerate(enemy):
        # 현재 라운드 e를 병사 소모에 먼저 반영
        n -= e
        # 지금까지 병사 소모에 반영한 라운드들을 저장
        # 나중에 n이 부족하면 여기서 가장 큰 e를 꺼내서 무적권 처리
        heapq.heappush(heap, -e)
        if n < 0:
            if k == 0:
                # 현재 라운드의 인덱스
                return i
            biggest = -heapq.heappop(heap)
            n += biggest
            k -= 1
    # 끝까지 다 수행했으면
    answer = len(enemy)
    return len(enemy)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2,4, [3, 3, 3, 3]))