import heapq
# import sys
# from io import StringIO
#
# sys.stdin = StringIO("""8
# .S..#.##
# ##.S.##.
# ##S#S##S
# ..SS.S##
# .S#S.#S#
# ..#S...#
# ###....S
# #.S.SS#.
# 5
# 1 1 1 3
# 4 1 4 5
# 6 2 1 1
# 7 4 8 8
# 8 2 6 1
# """)
# input = sys.stdin.readline
#1. 입력
N = int(input())
A = [list(input().strip()) for _ in range(N)]
Q = int(input())
#2. 공통 변수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = float('inf')

#3. 점프 가능 위치 전처리
#moves[r][c][k][d] = (nr, nc) or None
moves = [[[[None for _ in range(4)] for _ in range(6)] for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        #여기서 모든 r, c, k, d에 대해
        if A[r][c] != ".":
            continue
        for d in range(4):
            for k in range(1, 6):
                nr =  r + (dr[d] * k)
                nc = c + (dc[d] * k)
                #불가한 곳
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                if A[nr][nc] == "#":
                    break
                if A[nr][nc] == "S":
                    continue
                moves[r][c][k][d] = (nr, nc)

# =========================
# 2. change 전처리
# =========================
change = [[0 for _ in range(6)] for _ in range(6)]
for cur_k in range(1, 6):
    for next_k in range(1, 6):
        #cur_k -> next_k비용 저장
        if next_k == cur_k:
            change[cur_k][next_k] = 0
        elif next_k < cur_k:
            change[cur_k][next_k] = 1
        else:
            total = 0
            for x in range(cur_k + 1, next_k + 1):
                total += x * x
            change[cur_k][next_k] = total

# =========================
# 5. 쿼리 하나 푸는 함수
# =========================
def solve(r1, c1, r2, c2):
    dist = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(6)]
    heap = []
    dist[1][r1][c1] = 0
    heapq.heappush(heap, (0, 1, r1, c1))
    while heap:
        cost, cur_k, r, c = heapq.heappop(heap)
        if cost != dist[cur_k][r][c]:
            continue
        if r == r2 and c == c2:
            return cost
        for next_k in range(1, 6):
            move_cost = change[cur_k][next_k] + 1

            for d in range(4):
                nxt = moves[r][c][next_k][d]
                if nxt is None:
                    continue
                nr, nc = nxt
                next_cost = cost + move_cost
                if next_cost < dist[next_k][nr][nc]:
                    dist[next_k][nr][nc] = next_cost
                    heapq.heappush(heap, (next_cost, next_k, nr, nc))
    return -1
# =========================
# 4. Q개 쿼리 처리
# =========================
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -=1
    c1 -=1
    r2 -=1
    c2 -=1
    print(solve(r1, c1, r2, c2))

# def can_jump(r, c, nr, nc, next_k, d):
#     #가능한 점프
#     for step in range(1, next_k + 1):
#         cr = r + (dr[d] * step)
#         cc = c + (dc[d] * step)
#         # 이동하려는 위치에 돌이 없다면
#         # 파이썬 인덱스를 사용하므로
#         if cr < 0 or cr >= N or cc < 0 or cc >= N:
#             return False
#         #만약 이동하는 경로에 위험한게 있다면
#         if A[cr][cc] == "#":
#             return False
#     # 만약 미끄러운 돌이 있는 등 도착칸이 안전한 돌이 아니라면
#     if A[nr][nc] != ".":
#         return False
#     return True
#
# def change_cost(cur_k, next_k):
#     #유지
#     if next_k == cur_k:
#         return 0
#     #감소
#     if next_k < cur_k:
#         return 1
#     total = 0
#     #증가
#     # 현재 점프력 다음 값부터 목표 점프력까지
#     for x in range(cur_k+1, next_k+1):
#         total += x * x
#     return total
#
# for i in range(Q):
#     r1, c1, r2, c2 = map(int, input().split())
#
#     r1 -=1
#     c1 -=1
#     r2 -=1
#     c2 -=1
#     #print(r1, c1, r2, c2)
#     # 초기 점프력
#     k = 1
#     #처음 시작 비용은 0
#     # 최소 이동비용표
#     # 점프력이 최대 5까지이므로, 이렇게 구함.
#     INF = float('inf')
#     heap = []
#     dist = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(6)]
#     # print(type(dist))  # list
#     # print(type(dist[1]))  # list
#     # print(type(dist[1][r1]))  # list
#     # print(type(dist[1][r1][c1]))  # float
#     dist[k][r1][c1] = 0
#     heapq.heappush(heap, (0, k, r1, c1))
#
#     while heap:
#         cost, cur_k, r, c = heapq.heappop(heap)
#         # 만약 꺼낸것이,
#         if cost != dist[cur_k][r][c]:
#             continue
#         #최대 점프력은 5까지 증가 가능.
#         for next_k in range(1, 6):
#             change = change_cost(cur_k, next_k)
#             # 상하좌우 방향으로
#             for d in range(4):
#                 #다음 행은 상화좌우 하나를 k만큼 곱한것
#                 nr = r + (dr[d] * next_k)
#                 nc = c + (dc[d] * next_k)
#                 #만약 점프를 할 수 없으면 스킵한다.
#                 if not can_jump(r, c, nr, nc, next_k, d):
#                     continue
#                 next_cost = cost + change + 1
#                 if next_cost < dist[next_k][nr][nc]:
#                     dist[next_k][nr][nc] = next_cost
#                     heapq.heappush(heap, (next_cost, next_k, nr, nc))
#
#     answer = min(dist[k][r2][c2] for k in range(1, 6))
#     #print(N, r1, c1, r2, c2)
#     if answer == float('inf'):
#         print(-1)
#     else:
#         print(answer)