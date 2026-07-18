# 세로길이가 n, 가로길이가 m인 격차.
# 가장 많은 석율르 뽑을 수 잇는 시추관의 위치. 열 하나를 관통해야 함.
# land는 2차원 정수배열. 석유가 묻힌 땅과 석유덩어리를 나타냄.
# 2차원 격차 + 덩어리 탐색 + 중복 제거

# 1. 석유 덩어리 하나 찾기
# 2. 그 덩어리 크기 세기
# 3. 그 덩어리가 지나간 열 번호 모으기
# 4. 그 열들에 덩어리 크기 더하기
# 5. 모든 덩어리에 대해 반복
#  6. 가장 많이 모인 열 반환
from collections import deque

def solution(land):
    # 세로길이
    n = len(land)
    # 가로길이  = 열의 개수 . 어떤 열에 꽂았을때 석유가 가장 많이 나오는지 알아야 하니까.
    m = len(land[0])
    # 각 열에서 석유량이 얼마나 있는지 알아야 함.
    oil_by_col = [0] * m
    # land를 한칸 씩 보고, 아직 방문 안 한 1을 만나면 bfs시작, bfs로 연결된 1을 전부 찾음. 덩어리 크기와 닿은 열 번호들을 기록함. 그 열들에 덩어리 크기를 더함.
    # 이 칸이 덩어리 탐색을 진행했는지
    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and not visited[r][c]:
                # 대기줄시작.
                q = deque()
                # 탐색할 것을 큐에 넣음.
                q.append((r, c))
                # 방문 처리.
                visited[r][c] = True
                # 석유 덩어리 크기를 셀 변수임.
                oil_size = 0
                # 석유 덩어리가 걸쳐있는 열 번호들을 중복없이 저장.
                cols = set()

                while q:
                    cur_r, cur_c = q.popleft()
                    # 오일 덩어리 사이즈 증가.
                    oil_size += 1
                    # 오일 덩어리가 닿은 열 기록.
                    cols.add(cur_c)
                    for dr, dc in directions:
                        nr = cur_r + dr
                        nc = cur_c + dc
                        # 격자 바깥이 아닐때.
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] ==1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                # 덩어리 탐색이 끝난후에 이번 열이 닿은 덩어리들의 오일 크기를 더함.
                for col in cols:
                    oil_by_col[col] += oil_size

    # 가장 많이 얻는 열을 반환
    return max(oil_by_col)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
# 9

print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
# 16

