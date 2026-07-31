
# 메두사의 공원 이동 경로는 도로 제한이 있으므로 BFS로 계산한다.
# 전사의 이동 방향 선택은 맨해튼 거리 감소 여부로 판단한다.
from collections import deque

# 좌표 변수 기준
# r, c      : 현재 검사 중인 일반 좌표
# mr, mc    : 메두사의 현재 행, 열
# wr, wc    : 전사의 현재 행, 열
# nr, nc    : 한 칸 이동하거나 시야를 확장해서 만든 후보 행, 열

def manhattan(r1, c1, r2, c2):
    # 두 좌표 사이에서 상하 이동 횟수 + 좌우 이동 횟수를 계산한다.
    # 전사는 도로 여부를 보지 않으므로 이동 전후 거리를 이 값으로 비교한다.
    return abs(r1 - r2) + abs(c1 - c2)


# 한 방향의 기본 삼각형 시야표를 만드는 함수
# 여기서 방향을 최종 선택하지 않는다.
# 상, 하, 좌, 우 후보를 검사할 때마다 임시 sight를 하나씩 만든다.
# direction: 0=상, 1=하, 2=좌, 3=우
def make_sight(direction, mr, mc, N):
    # k=메두사로부터 떨어진 거리
    # sight[r][c] == True면 메두사의 시야 안에 있는 칸
    # sight는 정수 하나가 아니라 N x N True/False 표다.
    # True  : 해당 칸이 현재 direction의 기본 시야 범위 안
    # False : 해당 칸이 현재 direction의 기본 시야 범위 밖
    sight = [[False] * N for _ in range(N)]

    # k는 메두사 위치에서 시선 방향으로 몇 줄 떨어졌는지를 뜻한다.
    # k=1이면 바로 앞줄, k=2이면 두 줄 앞이다.
    for k in range(1, N):
        if direction == 0:
            #위쪽을 보니까 행이 줄어듦
            nr = mr - k
            #격자 밖이면 더 볼 수 없음
            if nr <0:
                break
            #위로 k칸 갈수록 왼쪽/오른쪽으로 k칸씩 퍼짐.
            for nc in range(mc - k, mc + k+1):
                #열이 격자 안이면 시야 처리
                if 0 <=nc <N:
                    sight[nr][nc] = True
        elif direction == 1:
            nr = mr + k
            if nr >= N:
                break
            for nc in range(mc - k, mc + k+1):
                if 0<=nc<N:
                    sight[nr][nc] = True
        elif direction ==2:
            nc = mc -k
            if nc <0:
                break
            for nr in range(mr - k, mr + k+1):
                if 0<=nr<N:
                    sight[nr][nc] = True
        elif direction ==3:
            nc = mc +k
            if nc >= N:
                break
            for nr in range(mr - k, mr + k+1):
                if 0<=nr<N:
                    sight[nr][nc] = True
    return sight


# 현재 direction에서 메두사에게 보이는 전사 한 명의 뒤쪽을 그림자로 표시한다.
# 이 함수는 시선 방향을 선택하지 않고, 전달받은 shadow 표만 수정한다.
#
# start_c, end_c
# → 현재 그림자로 칠하는 한 행 nr에서 열 범위의 시작과 끝
# → 메두사나 전사의 시작 위치라는 뜻이 아니다.
#
# start_r, end_r
# → 현재 그림자로 칠하는 한 열 nc에서 행 범위의 시작과 끝
def make_shadow(direction, mr, mc, wr, wc, shadow, N):
    # k는 전사 위치에서 시선 진행 방향으로 몇 칸 뒤인지 뜻한다.
    # k=1이면 전사 바로 뒤의 줄, k=2이면 전사 뒤 두 번째 줄이다.
    for k in range(1, N):
        # 메두사가 위를 보는 경우
        # 전사 뒤쪽도 위 방향으로 진행하므로 행 wr에서 k만큼 뺀다.
        if direction == 0:
            nr = wr - k
            if nr < 0:
                break

            # 전사의 열 wc와 메두사의 열 mc를 비교해서
            # 전사가 시야의 왼쪽/정면/오른쪽 중 어디에 있는지 구분한다.
            if wc < mc:
                start_c = wc - k
                end_c = wc
            elif wc == mc:
                start_c = wc
                end_c = wc
            else:
                start_c = wc
                end_c = wc + k

            # 현재 그림자 행 nr에서 start_c부터 end_c까지 True로 칠한다.
            # range의 끝값은 포함되지 않으므로 end_c + 1을 사용한다.
            for nc in range(start_c, end_c + 1):
                if 0 <= nc < N:
                    shadow[nr][nc] = True

        # 메두사가 아래를 보는 경우
        # 전사 뒤쪽도 아래 방향으로 진행하므로 행 wr에 k를 더한다.
        elif direction == 1:
            nr = wr + k
            if nr >= N:
                break

            if wc < mc:
                start_c = wc - k
                end_c = wc
            elif wc == mc:
                start_c = wc
                end_c = wc
            else:
                start_c = wc
                end_c = wc + k

            # 아래쪽의 현재 그림자 행 nr에서 열 범위를 칠한다.
            for nc in range(start_c, end_c + 1):
                if 0 <= nc < N:
                    shadow[nr][nc] = True

        elif direction == 2:
            nc = wc - k
            if nc < 0:
                break

            # 전사의 행 wr과 메두사의 행 mr을 비교해서
            # 전사가 시야의 위/정면/아래 중 어디에 있는지 구분한다.
            if wr < mr:
                start_r = wr - k
                end_r = wr
            elif wr == mr:
                start_r = wr
                end_r = wr
            else:
                start_r = wr
                end_r = wr + k

            # 현재 그림자 열 nc에서 start_r부터 end_r까지 True로 칠한다.
            for nr in range(start_r, end_r + 1):
                if 0 <= nr < N:
                    shadow[nr][nc] = True

        elif direction == 3:
            nc = wc + k
            if nc >= N:
                break

            if wr < mr:
                start_r = wr - k
                end_r = wr
            elif wr == mr:
                start_r = wr
                end_r = wr
            else:
                start_r = wr
                end_r = wr + k

            # 오른쪽의 현재 그림자 열 nc에서 행 범위를 칠한다.
            for nr in range(start_r, end_r + 1):
                if 0 <= nr < N:
                    shadow[nr][nc] = True


# 후보 방향 d 하나를 기준으로 다음 세 값을 계산한다.
# 1. stone_count      : 이 방향에서 돌이 되는 전사 수
# 2. final_sight      : 전사 그림자를 제외한 실제 시야표
# 3. stoned_warriors  : 이번 방향에서 돌이 된 전사의 좌표 집합
#
# 이 함수는 상/하/좌/우마다 한 번씩 호출된다.
def get_stone_info(d, mr, mc, warriors, sight, N):
    # shadow[r][c] == True면 전사 때문에 가려진 칸
    # 방향 하나를 검사할 때마다 새로운 shadow를 만든다.
    # 이전 방향의 그림자가 다음 방향 계산에 섞이지 않게 한다.
    shadow = [[False] * N for _ in range(N)]

    # 실제로 돌이 된 전사 위치 저장
    # 전사 이동을 막을 때 사용
    # 이 set은 전사 수를 세는 용도가 아니라
    # 선택된 방향에서 어느 좌표의 전사가 이번 턴에 멈추는지 확인하는 용도다.
    stoned_warriors = set()

    # 돌이 된 전사 수
    # 같은 칸에 전사가 여러 명 있을 수 있으므로 set 길이로 세면 안 됨
    # 같은 좌표에 전사가 여러 명 있을 수 있으므로 사람 수는 별도 정수로 센다.
    stone_count = 0

    # 메두사와 가까운 전사부터 처리
    # 가까운 전사가 뒤쪽 시야를 가릴 수 있기 때문
    # 가까운 전사를 먼저 처리해야 그 전사가 만든 shadow가
    # 뒤쪽 전사를 가리는지 순서대로 판정할 수 있다.
    warrior_order = sorted(
        warriors,
        key=lambda x: abs(x[0] - mr) + abs(x[1] - mc)
    )

    # 가까운 전사부터 한 명씩 현재 방향의 실제 시야에 들어오는지 확인한다.
    for wr, wc in warrior_order:
        # 시야 밖이면 돌이 안 됨
        # sight는 그림자를 적용하기 전의 기본 삼각형 시야다.
        # 전사 좌표가 기본 삼각형 밖이면 이 방향에서 보이지 않는다.
        if not sight[wr][wc]:
            continue

        # 그림자 안이면 돌이 안 됨
        # 기본 삼각형 안이어도 앞 전사의 shadow 안이면 메두사에게 보이지 않는다.
        if shadow[wr][wc]:
            continue

        # 시야 안이고 그림자 밖이면 돌이 됨
        stone_count += 1
        stoned_warriors.add((wr, wc))

        # 이 전사 뒤쪽을 그림자로 처리
        # 현재 전사는 보이는 전사이므로 돌이 된다.
        # 현재 전사 뒤쪽을 shadow에 추가해서 뒤에 있는 전사의 가림 여부를 계산한다.
        make_shadow(d, mr, mc, wr, wc, shadow, N)
    #전사가 실제로 이동할 수 없는 최종 시야

    # 세 시야 변수의 차이
    # sight       : 방향 d의 기본 삼각형 시야
    # final_sight : 방향 d에서 전사 뒤 shadow를 뺀 실제 시야
    # best_sight  : 네 방향의 final_sight 중 메두사가 최종 선택한 시야
    final_sight = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 기본 시야 안이고 그림자 밖인 칸만 실제 시야로 남긴다.
            if sight[r][c] and not shadow[r][c]:
                final_sight[r][c] = True
    # 호출부에서는 세 값을 같은 순서로 받아야 한다.
    return stone_count, final_sight, stoned_warriors



# 전사 한 명의 한 번 이동만 처리한다.
# 이 함수 한 번 호출 = 최대 한 칸 이동
# 전사는 한 턴에 이 함수를 1차 우선순위와 2차 우선순위로 두 번 호출한다.
# best_sight는 방향 번호가 아니라, 최종 선택된 방향의 실제 시야표다.
def move_warrior_once(wr, wc, mr, mc, priority, dirs, best_sight, N):
    # current_dist: 이동하기 전 전사 위치에서 메두사까지의 맨해튼 거리
    current_dist = manhattan(wr, wc, mr, mc)
    for d in priority:
        dr, dc = dirs[d]
        nr = wr + dr
        nc = wc + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        #이동하려는 칸이 메두사 시야 안이면
        #→ 전사는 그 칸으로 이동할 수 없음
        #→ 다음 방향 후보를 봄
        if best_sight[nr][nc]:
            continue
        # next_dist: 후보 칸 (nr, nc)로 한 칸 갔을 때 메두사까지의 거리
        next_dist = manhattan(nr, nc, mr, mc)
        # 이동 후 거리가 줄어들면 그 칸으로 이동
        #next_dist는 전사가 이동하려는 후보 칸에서 메두사까지의 거리
        if next_dist < current_dist:
            # 후보 칸으로 한 칸 이동한다.
            # 반환값 1은 전체 전사 이동거리 합에 더할 한 칸을 뜻한다.
            return nr, nc, 1
    ## 모든 방향을 봤는데 이동할 수 없으면 제자리
    # 우선순위의 모든 방향을 확인했지만 이동할 수 없으면 원래 좌표를 반환한다.
    # 반환값 0은 이번 호출에서 이동거리가 늘지 않았다는 뜻이다.
    return wr, wc, 0

# 전체 흐름
# 입력 → 공원 기준 BFS 거리표 생성 → 매 턴 반복
# 매 턴: 메두사 1칸 이동 → 전사 제거 → 시선 선택 → 전사 이동 → 출력
def solution():
    #마을의 크기, 전사의 수
    N, M = map(int, input().split())
    #메두사의 집의 위치정보와 공원의 위치정보
    sr, sc, er, ec = map(int, input().split())
    #메두사는 오직 도로만을 따라 최단경로로 공원까지 이동함.
    #메두사의 집과 공원은 항상 도로 위에 있음.
    #전사들의 좌표
    # 한 줄에 전사 M명의 좌표가 r1 c1 r2 c2 ... 형태로 들어온다.
    # 총 정수 개수는 2 * M개다.
    warrior_data = list(map(int, input().split()))
    warriors = []
    for i in range(0, 2 * M, 2):
        r = warrior_data[i]
        c = warrior_data[i +1]
        warriors.append((r, c))
        #전사들은 도로와 비도로 구분 안함.어느 칸이든 위치 가능
        #메두사는 전사들이 움직이기 전에, 바라봄으로써 돌로 만들어 움직임 멈출 수 있음.
    board = []
    for _ in range(N):
        # 한줄로 들어오는 것을 받아서 N번 반복하고
        row = list(map(int, input().split()))
        board.append(row)
    #1. 메두사의 이동
    #메두사는 공원까지 최단경로, 도로 한칸 이동, 이동한 칸에 전사 있으면, 전사는 공격 받고 사라짐.
    #집으로부터 공원까지 여러 최단경로 가능하면 상, 하, 좌, 우 우선순위를 따름.
    #다만 메두사의 집으로부터 공원까지 이어지는 도로 존재하지 않을 수 도 있음

    dirs = {
        0: (-1, 0),#상
        1: (1, 0),#하
        2: (0, -1),#좌
        3: (0, 1) #우
    }
    move_to_park_priority  = [0, 1, 2, 3]
    # dist[r][c]: 도로만 이용했을 때 (r, c)에서 공원까지 남은 최단거리
    # -1은 아직 BFS로 방문하지 못했거나 공원과 연결되지 않은 칸을 뜻한다.
    dist = [[-1] * N for _ in range(N)]
    queue = deque()
    # 공원에서 BFS를 시작한다.
    # 그러면 메두사는 현재 칸보다 dist가 1 작은 이웃을 골라 공원 쪽으로 이동할 수 있다.
    queue.append((er, ec))
    dist[er][ec] = 0
    # 이 while은 메두사가 실제로 움직이는 턴 반복이 아니다.
    # 공원까지의 거리표 dist를 한 번 미리 만드는 BFS 반복이다.
    while queue:
        r, c = queue.popleft()
        for d in move_to_park_priority:
            dr, dc = dirs[d]
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 이미 방문한 칸이면 건너뜀
            if dist[nr][nc] != -1:
                continue
            #도로가 아니면
            if board[nr][nc] != 0:
                continue
            #건널 수 있음
            dist[nr][nc] = dist[r][c]+1
            queue.append((nr, nc))
    #만약에 도착했는데
    if dist[sr][sc] ==-1:
        print(-1)
        return
    mr, mc = sr, sc
    # 메두사가 직접 한 칸 이동해야 함

    # 이 while 한 번이 게임의 한 턴이다.
    # 이전 턴의 석화 목록과 선택 시야는 아래에서 매 턴 새로 만든다.
    while (mr, mc) != (er, ec):
        #1. 메두사가 실제로 한 칸 이동
        for d in move_to_park_priority:
            dr, dc = dirs[d]
            nr = mr + dr
            nc = mc + dc
            if nr <0 or nr >= N or nc <0 or nc >= N:
                continue
            #공원까지 남은 거리가 1 줄어드는 칸으로 이동
            ## 현재 칸보다 공원까지의 거리가 1 작은 칸으로 이동한다.
            # 이렇게 해야 메두사가 공원까지의 최단경로를 따라 한 칸 이동한다.
            if dist[nr][nc] == dist[mr][mc] -1:
                mr, mc = nr, nc
                break
        # 메두사가 공원에 도착한 턴이면 0 출력 후 종료
        if (mr, mc) == (er, ec):
            print(0)
            return
        #2. 메두사가 이동한 칸에 있는 전사 제거
        new_warriors = []

        # 모든 전사를 한 명씩 처리한다.
        # moved_warriors에는 이번 턴이 끝난 뒤 살아 있는 전사만 넣는다.
        for wr, wc in warriors:
            # 전사의 최종 좌표가 메두사 좌표와 같으면 공격한 전사 수를 늘린다.
            # continue 때문에 이 전사는 moved_warriors에 남지 않는다.
            if wr == mr and wc == mc:
                continue
            new_warriors.append((wr, wc))
        warriors = new_warriors

        #2. 메두사의 시선
        # 메두사는 매 턴 상, 하, 좌, 우 네 방향을 전부 시험한다.
        # 방향별 돌이 되는 전사 수를 비교한 뒤 한 방향만 최종 선택한다.
        medusa_priority_sight = [0, 1, 2, 3]
        # 지금까지 검사한 방향 중 돌이 되는 전사 수의 최댓값
        # 첫 방향의 stone_count가 0이어도 갱신되도록 초기값을 -1로 둔다.
        best_stone_count = -1
        # 최종 선택된 방향에서 이번 턴에 돌이 된 전사 좌표
        # while 안에서 매 턴 다시 만들어지므로 석화 상태는 다음 턴에 자동으로 초기화된다.
        best_stoned_warriors = set()
        # 최종 선택된 방향의 실제 시야표를 저장할 자리
        # 방향 번호를 저장하는 변수가 아니다.
        # 전사가 이동할 후보 칸이 메두사의 시야인지 검사할 때 사용한다.
        best_sight = [[False] * N for _ in range(N)]
        # d=0,1,2,3을 차례로 검사한다.
        # 같은 수의 전사를 돌로 만들면 아래 조건이 '>'이므로 먼저 본 방향이 유지된다.
        for d in medusa_priority_sight:
            # 현재 후보 방향 d의 기본 삼각형 시야표
            # 다음 방향을 검사하면 새 sight가 다시 만들어진다.
            sight = make_sight(d, mr, mc, N)

            # 현재 후보 방향 d의 결과를 받는다.
            # stone_count     : 이 방향에서 돌이 되는 전사 수
            # final_sight     : 이 방향의 실제 시야표
            # stoned_warriors : 이 방향에서 돌이 된 전사 좌표
            stone_count, final_sight, stoned_warriors = get_stone_info(
                d, mr, mc, warriors, sight, N
            )


            # 현재 후보 방향이 지금까지의 최선보다 더 많은 전사를 돌로 만들면 갱신한다.
            if stone_count > best_stone_count:
                best_stone_count = stone_count
                best_stoned_warriors = stoned_warriors
                # 현재 후보 방향의 실제 시야를 최종 선택 시야로 저장한다.
                # 네 방향 검사가 끝나면 best_sight 하나만 전사 이동 제한에 사용된다.
                best_sight = final_sight

        # 더 많은 전사를 볼 수 있는쪽을 바라봄.

        #3. 전사들의 이동
        moved_warriors = []
        warrior_distance = 0
        attacked_medusa = 0
        # 전사의 첫 번째 한 칸 이동 우선순위: 상, 하, 좌, 우
        warriors_move_first_priority = [0, 1, 2, 3]
        # 전사의 두 번째 한 칸 이동 우선순위: 좌, 우, 상, 하
        warriors_move_second_priority = [2, 3, 0, 1]
        for wr, wc in warriors:
            # 최종 선택된 시야에서 돌이 된 전사는 이번 턴에 이동하지 않는다.
            # 좌표를 그대로 moved_warriors에 넣고 다음 전사로 넘어간다.
            if (wr, wc) in best_stoned_warriors:
                moved_warriors.append((wr, wc))
                continue

        #3-1. 전사들의 이동 첫번째 우선순위
            wr, wc, moved = move_warrior_once(
                wr, wc, mr, mc,
                warriors_move_first_priority,
                dirs,
                best_sight,
                N
            )
            # moved는 1차 이동 성공 시 1, 이동하지 못하면 0이다.
            # 모든 전사의 이동거리 합에 더한다.
            warrior_distance += moved

        #3-2. 전사들의 이동 두번째 우선순위
            wr, wc, moved = move_warrior_once(
                wr, wc, mr, mc,
                warriors_move_second_priority,
                dirs,
                best_sight,
                N
            )
            # moved는 2차 이동 성공 시 1, 이동하지 못하면 0이다.
            warrior_distance += moved
            #이동 후 메두사와 같은 칸이면 공격하고 사라짐
            if wr == mr and wc == mc:
                attacked_medusa += 1
                continue
            moved_warriors.append((wr, wc))
        warriors = moved_warriors

        # 출력 $
        # 전사가 이동한 거리의 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수를 공백을 사이에 두고 출력함
        print(warrior_distance, best_stone_count, attacked_medusa)
        # 하지만 메두사가 공원에 도착하면 0을 출력하고 프로그램을 종료함.

solution()