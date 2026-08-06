from collections import deque
import sys
# N =미지의 공간 NXN, M =MXM 크기의 연속 블록 형태, F=
N, M, F = map(int, input().split())
#print(N, M, F)

#1. 미지의 공간 평면도
# 각 값은 0(빈공간), 1(장애물), 3(시간의 벽), 4(탈출구) 중 하나임.
# 평면도에 값 3(시간의 벽)은 MxM은 하나만 존재함.
# 평면도에 4(탈출구)는 하나만 존재함.
floor_map = []
for col in range(N):
    row = list(map(int, input().split()))
    floor_map.append(row)
#print(floor_map)

# 타임월의 위치를 floor_map에서 표시할 방법은 없는가? (2, 2)에서 (4, 4)사이이긴 함.
# 타임월에서 2를 발견한 위치를 floor_map에 어떻게 표시하지.
# 333으로밖에 표시가 안되어있으니까, floor_map의 딱한개의 출구를 찾을때까지는 BFS를 통해 찾아야 할 것 같음.

time_wall_location = []
for col in range(N):
    for row in range(N):
        # 333으로 된 곳을 통해 알 수 있게됨.
        if floor_map[row][col] == 3:
            time_wall_location.append([row, col])
#print(time_wall_location)

#처음 나온거에서 행과 열을 하나씩 빼보고.
time_wall_location.sort()
#print(time_wall_location)

min_row, min_col = time_wall_location[0]
max_row, max_col = time_wall_location[-1]

#print(min_row, min_col, max_row, max_col)

# 장애물로 둘러쌓인 범위를 알기 위해서,
range_min_row = min_row - 1
range_max_row = max_row + 1
range_min_col = min_col - 1
range_max_col = max_col + 1

#print(range_min_row, range_min_col, range_max_row, range_max_col)

# 이 범위중에 0의 위치를 찾고 싶은데
one_gate = []
for one_gate_col_idx in range(range_min_col, range_max_col+1):
    for one_gate_row_idx in range(range_min_row, range_max_row+1):
        if floor_map[one_gate_row_idx][one_gate_col_idx] == 0:
            #이곳이 딱하나의 출구임.
            #print(one_gate_row_idx, one_gate_col_idx)
            one_gate = [one_gate_row_idx, one_gate_col_idx]
#print(one_gate)
#print(floor_map)
# floor_map에서 3으로 된 값이 시간의 벽면 윗면 단면도임. 그 중에 2가 타임머신 시작위치.
# floor_map에는 4가 있는데 탈출구임.
# 평면도와 단면도 둘 다, 0으로만 이동할 수 있음.
# 시간의 공간 테두리는 기본적으로 1인데 딱 한칸만 빈공간임.
# 딱 한칸만 빈 공간으로 뚫려 있어서 시간의 벽에서 미자의 공간 바닥으로 이어질 수 있는 출구는 하나임.


# 2. 시간의 벽의 동(0), 서(1), 남(2), 북(3), 그리고 윗면 단면도
# 각 값은 0(빈공간), 1(장애물) 중 하나
# 윗면은 MXM 행렬, 각 값은 0(빈공간), 1(장애물), 2(타임머신 시갖 귀치)중 하나. 2는 딱 하나
section_maps = {}
for section_idx in range(5):
    section_map = []
    for row in range(M):
        row = list(map(int, input().split()))
        section_map.append(row)
    section_maps[section_idx] = section_map
#print(section_maps)

#3. 시간이상 현상 F총 F개
time_anomalies = []
for _ in range(F):
    ri, ci, di, vi = list(map(int, input().split()))
    #print(ri, ci, di, vi)
    time_anomalies.append([ri, ci, di, vi])
#print(time_anomalies)

# 시간 이동때 참고할, 동, 서, 남, 북
d = [0, 1, 2, 3]

# 매턴 마다 상하좌우로 한칸씩 이동 가능함.
directions = {
    0: (0, 1),# 동
    1: (0, -1),  # 서
    2: (1, 0),  # 남
    3: (-1, 0),  # 북
}

#턴이 되면
t = 0
# 시간 이상 현상이 확산됨 .
# 이때 바닥에 있던 시간 이상 현상 중 한개가 확산되려고 해도 장애물이므로 확산되지 않고,
# 타임머신은 계속 이동할 수 있음
# 따라서 초기의 최단 이동 경로를 따라, 이동하면 t가 몇이 될때, 시간 이상 현상으로 인해,
# 더 이상 이동할 수 없는 현상이 발생함.

# 시간 이동때 참고할, 동, 서, 남, 북
# di = [0, 1, 2, 3]
# directions[d] 로 사용
#vi의 배수 턴마다 방향 di로 한칸씩 확산됨.
#sorted_time_anomalies = sorted(time_anomalies, key=lambda x: x[3])
#print(sorted_time_anomalies)

# 확산된 이후에도 기존 위치의 시간 이상 현상을 사라지지 않고 남아 있음. 빈공간으로 확산.


# 모든 시간 이상 현상으 서로 독립적이며 동시에 확산됨. ??이건 무슨 말이지?? 배수 턴마다 확산되는거잖아.
# 반복문 안에 넣지 말라는 얘기인가. 안그래도 고민하고 있었는데.
#그럼 함수로 빼야겠지.함수로 빼도 독립적이고 동시에 확산되나? 턴이 다른데 어떻게...
INF = 10**9

# 각 바닥 칸에 이상 현상이 처음 도착하는 시간
def make_anomaly_time(time_anomalies, directions, floor_map):
    anomaly_time = [[INF] * N for _ in range(N)]

    for ri, ci, di, vi in time_anomalies:
        anomaly_time[ri][ci] = 0

        dr, dc = directions[di]
        r, c = ri, ci
        # 이 이상 현상이 현재 칸까지 도착하는 데 걸린 누적 시간
        elapsed = 0

        while True:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break

            # 빈 공간으로만 확산
            if floor_map[nr][nc] != 0:
                break
            # 이상 현상은 vi의 배수 턴마다 한 칸 확산된다.
            elapsed += vi
            # 여러 이상 현상이 같은 칸에 도달할 수 있으므로
            # 그 칸에 가장 먼저 도착하는 시간만 저장한다.
            anomaly_time[nr][nc] = min(
                anomaly_time[nr][nc],
                elapsed
            )

            r, c = nr, nc

    return anomaly_time


anomaly_time = make_anomaly_time(
    time_anomalies,
    directions,
    floor_map
)
# 여기 다듬어야 함.
# 4. 타임머신 이동
# 매 턴마다 상하좌우 한칸씩 이동 가능.
# directions = {
#     0: (0, 11),# 동
#     1: (0, -1),  # 서
#     2: (1, 0),  # 남
#     3: (-1, 0),  # 북
# }

# 일단 초기 최단 경로가 이미 있음.
#print(section_maps)
time_wall = section_maps[4]
#print(time_wall)

start = None
sr = None
sc = None
for col in range(M):
    for row in range(M):
        #만약 타임월의 타임머신 시작위치를 찾는다면
        #아 , 그 전에 타임월의 위치들을 floor_map의 위치로 바꾸려고 함.
        # row +2, col +2 == floor_map[row][col]
        #print(row+2, col+2)
        if time_wall[row][col] == 2:
            # 거기를 시작위치로 하고 floor_map의 위치로 바꿈.
            sr, sc = row, col
            start = time_wall[sr][sc]
            #print(sr, sc, start)
            # 0, 0, 2
            # 거기서 시작하는데 0인 곳으로 상하좌우로 한칸씩 이동해서 floor_map에서 0인 칸을 발견함.
# print(start, sr, sc)
            # 주위는 장애물이 있고 딱 1칸만 경로가 있음.
            # 둘러쌓인 곳은 floor_map이고, 빈칸을 어떻게 찾냐고 하면 상하좌우로 한칸씩 턴마다 이동하면서
            # 0인곳을 찾아서, floor_map에서 4가 있는 곳까지 최단거리 BFS로 가면 됨.

# 일단 start에서 gate까지 가는 최단거리르 가는 턴 수를 찾아야 함.
start_r, start_c = sr, sc
#print(start_r, start_c)
gate_row = one_gate[0]
gate_col = one_gate[1]
#print(gate_row, gate_col)
#4, 5

gate_r, gate_c = one_gate
gate_row_in_time_wall, gate_col_in_time_wall = None, None

# one_gate과 section_maps의 어느 면과 연결되는지+ 그 면의 마지막 행 좌표

def find_wall_exit(gate_row, gate_col):
    # one_gate에서 바라봤을때 3이 있는 방향의 반댓방향이 실제 윗면의 옆면임
    opposite  = {
        0:1, # 게이트 동쪽에 3-> 써쪽면
        1:0, # 게이트 서쪽에 3->동쪽 면
        2:3, # 게이트 남쪽에 3->북쪽면
        3:2, # 게이트 북쪽에 3->남쪽면
    }
    for di, (dr, dc) in directions.items():
        # adj_r, adj_c는 floor_map에서 게이트와 붙어있는 3의 좌표임. 위에서 바라본 것임.
        adj_r = gate_row + dr
        adj_c = gate_col + dc
        # 벽의 행은 범위에 맞게 있어야 한다.
        if adj_r <0 or adj_r >= N or adj_c <0 or adj_c >= N:
            continue
        #만약 값이 3이 아니면 찾지 않는다.
        if floor_map[adj_r][adj_c] != 3:
            continue
        # 탈출하는 면적은 방향을 넣은 것이다.
        exit_face = opposite[di]
        # 탈출하는 행은
        exit_row = M -1
        # 만약, 탈출하는 면이 서쪽면이면,
        if exit_face == 0: #동쪽 면
        # 최대 row에서 3의 행을 빼면 그게 열 좌표
            exit_col = max_row - adj_r
        # 3의 행 좌표에서 min_row를 빼면 그게 열 좌표
        elif exit_face == 1: #서쪽 면
            exit_col = adj_r - min_row
        # 3의 열번호에서 min_col을 빼면 그게 열 좌표
        elif exit_face == 2: #남쪽면
            exit_col = adj_c - min_col
        # max-col에서
        elif exit_face == 3: #북쪽면
            exit_col = max_col - adj_c
        # 옆면에서의 기준임.

        return exit_face, exit_row, exit_col

    return -1, -1, -1
exit_face, exit_row, exit_col = find_wall_exit(gate_row, gate_col)
#print("출력", exit_face, exit_row, exit_col)

# BFS목표 section_maps[exit_face][exit_row][exit_col]

# time_wall안에서 gate위치까지 가는법
def bfs_time_wall(
    start_r,
    start_c,
    exit_face,
    exit_row,
    exit_col,
    directions
):
    dist = [
        [[-1] * M for _ in range(M)]
        for _ in range(5)
    ]
    q = deque()
    # print(visited)
    # 윗면 번호와 함께 스타트를 넣는다.

    q.append((4, start_r, start_c))
    dist[4][start_r][start_c] = 0

    while q:
        face, r, c = q.popleft()
        #현재 위치가 옆면 출구 좌표인지 확인
        if (
            face == exit_face
            and r == exit_row
            and c == exit_col
        ):
            return dist[face][r][c]

        for di, (dr, dc) in directions.items():
            nr = r + dr
            nc = c + dc
            #현재 면 안에서 이동한는 경우
            if 0<= nr < M and 0<= nc < M:
                next_face = face
                next_r = nr
                next_c = nc
            # 현재 면 밖으로 넘어가는 경우
            else:
                # 아직 윗면에 있는 경우
                if face == 4:
                    if di == 0: #동쪽
                        next_face = 0
                        #동쪽면의 윗줄로 들어감
                        next_r = 0
                        # 윗면의 행 순서를 반대로 뒤집어 동쪽 면의 열 번호로 사용
                        next_c = M-1-r
                    elif di ==1: #서쪽
                        next_face = 1
                        #서쪽면의 윗줄로 들어감
                        next_r = 0
                        next_c = r
                    elif di == 2:#남쪽
                        next_face = 2
                        #남쪽면의 윗줄로 들어감
                        next_r = 0
                        next_c = c
                    elif di == 3: #북쪽
                        next_face = 3
                        #북쪽면의 윗줄로 들어감
                        next_r = 0
                        next_c = M-1-c
                elif face == 0: # 현재 동쪽에 있는 경우
                    if di == 0: #오른족이니까,
                        next_face = 3 #북쪽
                        next_r = r
                        next_c = 0
                    elif di == 1: #왼쪽
                        next_face = 2 #남쪽
                        next_r = r
                        next_c = M-1
                    elif di == 2: #바닥
                        continue
                    elif di == 3: #윗면
                        next_face = 4
                        next_r = M-1- c
                        next_c = M-1
                elif face == 1: #현재 서쪽에 있는 경우
                    if di ==0: #오른쪽이니까
                        next_face = 2 # 남쪽
                        next_r = r
                        next_c = 0
                    elif di == 1: #왼쪽이니까
                        next_face = 3 #북쪽
                        next_r = r
                        next_c = M-1
                    elif di == 2: #바닥이니까
                        continue
                    elif di == 3: #윗쪽이니까
                        next_face = 4
                        next_r = c
                        next_c = 0
                elif face == 2: #현재 남쪽에 있는 경우
                    if di == 0: #오른쪽이니까
                        next_face = 0 #동쪽
                        next_r = r
                        next_c = 0
                    elif di == 1: #왼쪽이니까
                        next_face = 1 #서쪽
                        next_r = r
                        next_c = M-1
                    elif di == 2: #바닥이니까
                        continue
                    elif di == 3: #윗쪽이니까
                        next_face = 4
                        next_r = M-1
                        next_c = c
                elif face == 3: #현재 북쪽에 있는 경우
                    if di == 0: #오른쪽이니까
                        next_face = 1 #서쪽
                        next_r =r
                        next_c = 0
                    elif di == 1: #왼쪽이니까
                        next_face = 0 #동쪽
                        next_r =r
                        next_c = M-1
                    elif di == 2: #아래쪽이니까
                        continue
                    elif di == 3: #위쪽이니까
                        next_face = 4
                        next_r =0
                        next_c =M-1-c
            # 한번 방문한 곳은 또 방문안함.
            if dist[next_face][next_r][next_c] != -1:
                continue
            # 장애물을 피해야 함. 탈출구도 지나갈 수 있도록함.
            if section_maps[next_face][next_r][next_c] != 0:
                continue
            dist[next_face][next_r][next_c] = dist[face][r][c] + 1
            q.append((next_face, next_r, next_c))

    return -1

turn_in_section_maps =bfs_time_wall(
    start_r,
    start_c,
    exit_face,
    exit_row,
    exit_col,
    directions
)
#print(turn_in_section_maps)
start_time = turn_in_section_maps
# 이 부분은 생각 못했음.##############
#시간의 벽에서 탈출 할 수 없는 경우
if start_time == -1:
    print(-1)
    sys.exit()
###################

# 시간 이상 현상을 피해야 함
# 시간 이상 현상이 생긴 직후에, 경로를 변경해야 함. (이건 내 사견)

#실제로는 gate_row와 gate_col 근처 time_wall의 위치이지만 편의상 그렇게 표현함.
# 탈출구까지 도달해야 함.
def bfs_gate_to_exit(gate_row, gate_col, floor_map, directions):
    N = len(floor_map)

    #옆면 마지막 칸에서 바닥 gate로 내려오는 데 1턴 필요
    entry_time = start_time + 1
    # gate에 이상 현상이 먼저 또는 동시에 도착했다면 진입 불가
    if entry_time >= anomaly_time[gate_row][gate_col]:
        return -1
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    # print(visited)
    q.append((gate_row, gate_col))
    dist[gate_row][gate_col] = entry_time

    while q:
        r, c = q.popleft()
        current_time = dist[r][c]
        if floor_map[r][c] == 4:
            return current_time

        for di in range(4):
            dr, dc = directions[di]

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 한번 방문한 곳은 또 방문안함.
            if dist[nr][nc] != -1:
                continue
            # 장애물을 피해야 함. 탈출구도 지나갈 수 있도록함.
            if floor_map[nr][nc] != 0 and floor_map[nr][nc] != 4:
                continue
            next_time = current_time + 1

            # 이상 현상이 먼저 또는 같은 시간에 도착하면 이동 불가
            if next_time >= anomaly_time[nr][nc]:
                continue

            dist[nr][nc] = next_time
            q.append((nr, nc))

    return -1
gate_to_exit = bfs_gate_to_exit(gate_row, gate_col, floor_map, directions)
print(gate_to_exit)

# 타임머신이 시작점에서 탈출구까지 이동하느데 필요한 최소 시간(턴수)를 출력해야 함.
# 탈출할 수 없다면 -1을 출력해야 함.
# 시간 이상 현상이 확산된 직후, 타임머신이 이동해서, 타임머신은 시간 이상 현상이 확산되는 곳으로 이동할 수 없음
