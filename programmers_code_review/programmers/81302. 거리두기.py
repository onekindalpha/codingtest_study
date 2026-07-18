# 대기실 5개, 각 5x5크기
# 맨해튼 거리가 2이하로 앉지 않을 것
# 단, 응시자 앉아있는 자리 사이가 파티션으로 막혀있을때는 가능.

# 앉아있는 자리 P
# 빈 테이블 0
# 파티션 X

# 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열
# places가 매개변수로 주어짐.
# 각 대기실별로 거리두기를 지키고 있으면 1, 한명이라도 지키지 않고 있으면 0

# places를 검사해서 대기십별로 1, 0을 표시한다.
# len(places) = 5

# 각 대기실에서 P를 찾는다.
# 각 P를 시작점으로 BFS를 돌린다.
# 거리 2까지만 탐색한다.
# 현재 P에서 상하좌우 1칸 확인하고, 그 다음 상하좌우 1칸을 더 확인한다.
# X는 파티션이므로 지나가지 않느다.
# 거리 2 안에서 다른 P를 만나면 거리두기 위반이다.
from collections import deque
def bfs(room, sr, sc):
    q = deque()
    q.append((sr, sc, 0)) # 행, 열, 거리
    # 5X5 2차원배열 방문표를 만듦.
    visited = [[False] * 5 for _ in range(5)]
    #시작점은 방문처리를 함.
    visited[sr][sc] = True
    #왼쪽, 오른쪽, 위쪽, 아래쪽
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        r, c, dist = q.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            ndist = dist + 1
            # 배열 범위 안인지
            if nr < 0 or nr>= 5 or nc < 0 or nc>=5:
                continue
            # 이미 방문했었으면 지나침
            if visited[nr][nc]:
                continue
            # 거리가 2 초과면 지나침. 검사 안함.
            if ndist > 2:
                continue
            # 만약 파티션 있으면 지나침. 파티션 있으면 거리두기 2 이하여도 괜찮음.
            if room[nr][nc] == 'X':
                continue
            # 거리 2 이하인 상태에서,, P를 만났다니, 위반으로 False를 되돌려주마.
            if room[nr][nc] == 'P':
                return False

            visited[nr][nc] = True
            q.append((nr, nc, ndist))
    return True

# 결과 리스트에 0을 넣는다.
# 거리두기 위반이 없을 경우 1을 넣는다.
def check_room(room):
    for r in range(5):
        for c in range(5):
            # 어떠한 좌표가 P이고
            if room[r][c] == 'P':
                # 그 P를 시작점으로 행 과 열을 넘겨줘서, BFS 검사
                if not bfs(room, r, c):
                    # 위반이면 bfs가 False를 반환
                    return 0
    return 1

def solution(places):

    answer = []
    # 대기실 전체에서 대기실 하나를 꺼냄.
    for room in places:
        answer.append(check_room(room))
    return answer

places = [
    ["POOOP",
     "OXXOX",
     "OPXPX",
     "OOXOX",
     "POXXP"],

    ["POOPX",
     "OXPXP",
     "PXXXO",
     "OXXXO",
     "OOOPP"],

    ["PXOPX",
     "OXOXP",
     "OXPOX",
     "OXXOP",
     "PXPOX"],

    ["OOOXX",
     "XOOOX",
     "OOOXX",
     "OXOOX",
     "OOOOO"],

    ["PXPXP",
     "XPXPX",
     "PXPXP",
     "XPXPX",
     "PXPXP"]
]

print(solution(places))  # [1, 0, 1, 1, 1]