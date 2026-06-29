# 현재 칸과 이동하려는 칸의 높이 차가 height이하여야 함
# 높이차가 height보다 많이 나는 경우에는 사다리를 설치해서 이동 가능
# 두 격차 간의 높이차만큼 비용이 듦.
# 최대한 적은 비용이 들어야 함
# 최대 높이차 height
# 모든 칸 방문하기 위해 필요한 사다리 설치 비용의 최솟값
# land는 각 격차칸의 높이가 담긴 2차원 배열

from idlelib.help import copy_strip

# 최소 비용을 알아야 하니까.

import heapq

def solution(land, height):
    n = len(land)

    visited = [[False] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    answer = 0
    directions = [
        (-1, 0),  # 위
        (1, 0),  # 아래
        (0, -1),  # 왼쪽
        (0, 1)  # 오른쪽
    ]

    while heap:
        cost, row, col = heapq.heappop(heap)
        if visited[row][col]:
            continue
            # 처음 방문처리, 비용처리
        visited[row][col] = True
        answer += cost
        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc
            if 0<= next_row < n and 0 <= next_col <n:
                if not visited[next_row][next_col]:
                    # 현재 사다리 칸 높이  - 다음사다리 높이 = 두 칸의 높이 차이
                    diff = abs(land[row][col] - land[next_row][next_col])

                    if diff <= height:
                        next_cost = 0
                    else:
                        next_cost = diff

                    heapq.heappush(heap, (next_cost, next_row, next_col))

    return answer

print(solution(
    [[1, 4, 8, 10],
     [5, 5, 5, 5],
     [10, 10, 10, 10],
     [10, 10, 10, 20]],
    3
))
# 예상 결과: 15

print(solution(
    [[10, 11, 10, 11],
     [2, 21, 20, 10],
     [1, 20, 21, 11],
     [2, 1, 2, 1]],
    1
))
# 예상 결과: 18
