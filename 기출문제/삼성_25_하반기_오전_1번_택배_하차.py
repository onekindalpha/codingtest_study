#2. 택해 하차(좌측)

# 쌓인 택배 중에 잡고 왼쪽으로 이동했을 때 다른 택배와 부딪히지 않고 뺄 수 있는 택배를 먼저 하차합니다
# 그러한 택배가 여러개일 경우, 택배 번호(k)가 작은 택배를 먼저 하차합니다.

#해당 택배를 하차한 이후, 공간에 남아있는 택배들 중 떨어질 수 있는 것들은 떨어집니다.

#3. 택배 하차 (우측)

# 2의 과정을 우측에서도 진행합니다.

# 공간에 있는 택배를 모두 하차할 때까지 2, 3의 과정을 반복합니다.
# 다음과 같은 방법으로 택배를 하차할 때, 하차되는 택배의 번호를 순서대로 출력하는 프로그램을 작성하세요
answer = []
#0. 입력
N, M = map(int, input().split())
#택배 정보 저장
packages =[]
for i in range(M):
    k, h, w, c = map(int, input().split())
    packages.append({
        "id":k, #택배번호
        "h":h, ## 세로 크기 = 아래쪽으로 몇 행을 차지하는가
        "w": w, #가로 크기 = 오른쪽으로 몇 열을 차지하는가
        "r":0, ## 현재 택배의 가장 위쪽 행
        "left_c":c-1 # 현재 택배의 가장 왼쪽 열, 배열 인덱스용
        })
board = [[0] * N for _ in range(N)]
# ==================
# 1. 택배 투입 : 실제로 보드에 택배를 떨어뜨리는 코드를 작성한다.
# 택배는 직사각형 모양
# 직사각형 왼쪽 열의 위치 c, 가로 크기(w)와 세로 크기(h)으로 주어집니다
# 각각의 택배는 택배 번호(k)를 가집니다.
# ===================
def package_input(board,packages):
    # 택배 목록에서 택배를 하나 꺼낸다.
    for package in packages:
        # 그 택배의 번호, 세로 길이, 가로 길이, 시작 열을 확인한다.
        k = package["id"]
        h = package["h"]
        w = package["w"]
        r = package["r"]
        c = package["left_c"]
        #이 택배를 처음에는 보드의 맨 위에 있다고 생각한다.
        #아래로 계속 떨어뜨리기
        while True:
            # 이 택배를 아래로 한 칸 내려볼 수 있는지 확인한다.
            bottom_next_row = r + h
            # 택배의 맨 아래 행은 r+h-1이다.
            # 먼저, 택배 바로 아래쪽 한 줄이 보드 안에 있는지 확인한다.
            if bottom_next_row >= N:
                break
            # 만약 아래쪽 한 줄이 보드 밖이면,
            # 이 택배는 더 이상 내려갈 수 없다.
            # 보드 안이라면,
            # 택배 바로 아래쪽 한 줄을 확인한다.
            # 이때 택배 전체를 다 보는 게 아니라,
            # 택배의 가로 길이만큼 아래쪽 칸들을 본다.
            right_end = c + w
            # 일단 내려갈 수 있다고 가정한다. (센스)
            can_down = True
            #아래족에서 열을 하나씩 확인한다.
            for check_c in range(c, right_end):
                # 그 칸이 다른 번호들로 채워져있다면, 다른 짐을 만난 것이다.
                if board[bottom_next_row][check_c] != 0:
                    can_down = False
                    break
            # 그러다가
            # 아래쪽 한 줄이 보드 밖이거나,
            # 아래쪽 한 줄 중 하나라도 이미 다른 택배가 있으면,
            # 그 택배는 더 이상 내려갈 수 없다.
            if not can_down:
                break
            # 여기까지 왔다는 것은 아래쪽 칸들이 전부 비어 있다는 뜻이다.
            # 그러므로 택배를 한 칸 아래로 내린다.
            r += 1
        # while이 끝난 그 순간의 위치가 이 택배의 최종 위치다.
        package["r"] = r
        # 최종 위치에 택배 번호를 보드에 채운다. 모든 칸에 채워야 한다.
        for fill_r in range(r, r+h):
            for fill_c in range(c, c+w):
                board[fill_r][fill_c] = k
        # 그 다음 택배를 꺼내서 같은 과정을 반복한다.

#==============
# 2. 택배 하차(좌측)
#==============

# 1. 좌측 하차 가능한 후보를 찾는다.
# 2. 후보 중 번호가 가장 작은 target을 고른다.
# 3. target을 board에서 지운다.
# 4. target["removed"] = True로 표시한다.
# 5. target이 빠지면서 빈 공간이 생겼을 수 있으므로,
#    남은 택배들에 중력 처리를 적용한다.

def can_out(board, package, direction, N):
    #택배 하나를 잡는다.
    h = package["h"]
    w = package["w"]
    r = package["r"]
    c = package["left_c"]

    #일단 이 택배는 왼쪽으로 뺄 수 있다고 가정한다.
    can_exit = True

    # 이 택배가 차지하는 행은 r부터 r+h-1까지. 봐야할 행을 check_r로 정함.
    for check_r in range(r, r+h):
        # direction에 따라 확인할 열 범위가 달라진다.
        if direction =="left":
            check_range = range(0, c)
        elif direction =="right":
            check_range = range(c+w, N)
        # 해당 방향의 길을 확인한다.
        for check_c in check_range:
            # 나가는 길에 다른 택배가 있으면 못 뺀다.
            if board[check_r][check_c] != 0:
                can_exit = False
                break
        # 이미 못 뺀다는 걸 알았으면 다른 행은 더 볼 필요 없다.
        if not can_exit:
            break
    # 모든 왼쪽 길 검사가 끝났는데도 can_out이 True라라면 true를 돌려준다.
    return can_exit
    ## 해당 방향 길 검사가 끝났는데도 can_exit이 True라면 True를 돌려준다.

# ==============
# 3. 중력 처리
# ==============

# 남아 있는 택배들을 하나씩 본다.
# 각 택배를 잠깐 board에서 지운다.
# 아래로 갈 수 있는 만큼 내린다.
# 새 위치에 다시 채운다.
# 더 이상 움직이는 택배가 없을 때까지 반복한다.

# 공간에 남아있는 택배들 중, 떨
def apply_gravity(board, packages, N):
    while True:
        moved =False
        # 남아있는 택배들을 하나씩 본다.
        for package in packages:
            # 하차완료된 택배들은 건너뛴다.
            if package.get("removed"):
                continue
            # 각 택배에 대해,
            k = package["id"]
            h = package["h"]
            w = package["w"]
            r = package["r"]
            c = package["left_c"]
            # 이 택배의 처음 행 위치를 기억한다.
            original_r = r
            # 현재 위치에서 아래로 한 칸 내려갈 수 있는지 확인한다.
            # 단, 이 택배를 검사할때는
            # 자기 자신이 차지하던 칸은 잠깐 비워야 한다.
            # 왜냐하면 보드에 자기 번호가 그대로 남아있으면
            # 움직일 때 자기 자신과 충돌하는 것처럼 보일 수 있기 때문이다 (중요)
            # 자기 칸을 잠깐 0으로 비운다.
            for fill_r in range(r, r + h):
                for fill_c in range(c, c + w):
                    board[fill_r][fill_c] = 0
            # 그 다음 아까 택배 투입 때처럼 아래로 내려갈 수 있는 만큼 반복한다.
            while True:
                # 택배 바로 아래쪽 한 줄을 확인한다.
                bottom_next_row = r + h
                # 아래쪽 줄이 보드 밖이면 못 내려간다.
                if bottom_next_row >= N:
                    break
                # 보드 안이면,
                # 가로 길이 만큼 아래쪽 칸들을 확인한다.
                right_end = c + w
                # 일단 내려갈 수 있다고 가정한다. (센스)
                can_down = True
                # 아래족에서 열을 하나씩 확인한다.
                for check_c in range(c, right_end):
                # 그 칸이 다른 번호들로 채워져있다면, 다른 짐을 만난 것이다.
                    if board[bottom_next_row][check_c] != 0:
                        can_down = False
                        break
                # 그 칸들이 전부 0이면, (이것도 중요), 한칸 아래로 내린다.
                if not can_down:
                    break
                # 또 아래쪽 줄을 확인한다.
                r += 1
            # while이 끝난 그 순간의 위치가 이 택배의 최종 위치다.
            # 처음 위치 original_r과 현재 위치 r을 비교한다.
            #만약 r이 original_r과 다르면, 이 택배는 실제로 떨어진 것이다.
            if r != original_r:
                moved = True
            # package["r"]에 새 r을 저장한다.
            package["r"] = r
            # 최종 위치에 택배 번호 k를 다시 채운다.
            for fill_r in range(r, r + h):
                for fill_c in range(c, c + w):
                    board[fill_r][fill_c] = k
        # 남아있는 택배를 한바퀴 다 봤다.
        # 만약 moved = False라면, 이번 바퀴에서 아무 택배도 안 움직인 것이다.
        # 그러면 더이상 떨이질 택배가 없으므로 중력 처리를 끝낸다.
        if not moved:
            break
            # 더 이상 떨어지는 택배가 하나도 없으면 중력 처리가 끝난다.
# 택배를 하차한 이후,
def remove_package(board, target):
    #target은 하차할 택배 하나다.
    h = target["h"]
    w = target["w"]
    r = target["r"]
    c = target["left_c"]

    # 그 택배를 보드에서 지운다. = 그 택배가 차지하던 직사각형 영역을 전부 0으로 바꾼다.
    for fill_r in range(r, r + h):
        for fill_c in range(c, c + w):
            board[fill_r][fill_c] = 0
    # 이 택배는 하차 완료로 표시한다.
    target["removed"] = True
# 쌓인 택배 중에서 direction 방향으로 이동했을 때
# 다른 택배와 부딪히지 않고 뺄 수 있는 택배들을 찾는다.
#
# 그러한 택배가 여러 개일 경우,
# 택배 번호(id)가 가장 작은 택배 하나를 먼저 하차한다.
#
# 해당 택배를 하차한 뒤,
# 남아있는 택배들에 중력 처리를 적용한다.

def unload(board, packages, direction, N, answer):
    #direction방향으로 하차 가능한 후보들을 담을 빈 목록을 만든다.
    out_candidates = []
    #남아있는 모든 택배를 검사한다.
    for package in packages:
        # 이미 하차한 택배는 검사하지 않느다.
        if package.get("removed"):
            continue

        # 이 택배가 direction방향으로 빠질 수 있다면 후보에 넣는다.
        if can_out(board, package, direction, N):
            out_candidates.append(package)
    #모든 택배검사가 끝난다.
    # 좌측 하차 가능한 후보가 있다면 가장 작은 택배를 고른다.
    if out_candidates:
        # target = min(left_out_candidates, key=lambda package: package["id"])[^1]
        # [^1]: `min(후보목록, key=비교기준)`은 후보목록에서 비교기준이 가장 작은 원소를 고른다는 뜻이다. 여기서는 비교기준이 `package["id"]`이므로, 택배 번호가 가장 작은 택배 전체가 `target`에 저장된다.
        target = min(out_candidates, key=lambda package: package["id"])
        #고른 택배 하나를 하차한다.
        remove_package(board, target)
        # 하차된 택배 번호를 출력 순서 목록에 저장한다.
        answer.append(target["id"])
        #하차 후 생긴 빈 공간 때문에 중력 처리를 한다.
        apply_gravity(board, packages, N)
        # 이번 방향에서 실제로 택배를 하나를 하차했다는 뜻
        return True
    # 이번 방향에서는 하차할 수 있는 택배가 없었음
    return False

# ==================
# 4. 전체 하차 반복
# ==================
package_input(board, packages)
#공간에 있는 택배를 모두 하차할 때까지
# 2, 3의 과정을 반복합니다.
while True:
    #이번 반복을 시작하기 전에,
    #모든 택배가 하차 완료되었는지 확인한다.
    all_removed = True
    # packages를 하나씩 보면서, 아직 하차되지 않은 택배가 있는지 검사한다.
    for package in packages:
        if not package.get("removed"):
            all_removed = False
            break
    #모든 택배가 하차 완료라면 더이상 좌측/우측 하차를 할 필요가 없으므로 전체 반복을 끝낸다.
    if all_removed:
        break
    #2. 좌측 하차를 1번 시도한다.
    # unload함수안에서 나마있는 모든 택배르 ㄹ검사하고
    # 왼쪽으로 뺄 수 있는 후보 중 번호가 가장 작은 택배 하나를 하차한다.
    left_removed = unload(board, packages, "left", N, answer)
    #3. 우측 하차를 1번 시도한다.
    # unload함수 안에서 남아있는 모든 택배를 검사하고,
    #오른쪽으로 뺄 수 있는 후보 중 번호가 가장 작은 택배 하나를 하차한다.
    right_removed = unload(board, packages, "right", N, answer)

    #혹시 좌측/우측 둘 다 아무 택배도 못 뺐다면
    # 이번 반복에서 board, packages, answer가 변하지 않은 것이다.
    # 상태 변화가 없으면 다음 반복도 똑같이 반복될 수 있으므로 종료한다.
    #무한 반복을 막기 위해 종료한다.
    if not left_removed and not right_removed:
        break
#하차된 택배 번호를 순서대로 출력한다.
#(*answer)은 리스트를 풀어서 출력
print(*answer)