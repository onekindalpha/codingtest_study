from collections import deque

def food_rank(food):
    if len(food) == 1:
        return 0
    if len(food) == 2:
        return 1
    return 2

def merge_food(a, b):
    result = set()
    for food in a:
        result.add(food)
    for food in b:
        result.add(food)
    merged = ""
    for food in ["T", "C", "M"]:
        if food in result:
            merged += food
    return merged

def solution():
    N, T = map(int, input().split())
    #학생이 신봉하는 음식.
    #input().strip()을 N번 실행한다.
    #각 줄 문자열을 list로 바꾼다.
    #N개의 줄을 모아서 2차원 배열 F를 만든다.
    F = [list(input().strip()) for _ in range(N)]
    #학생의 신앙심
    B = [list(map(int, input().split())) for _ in range(N)]
    dirs =[
    (-1, 0),  # 상
    (1, 0),  # 하
    (0, -1),  # 좌
    (0, 1),  # 우

    ]
    # T일 동안 아침, 점심, 저녁 실행
    #T일 동안 실행해야 하니까 반복 횟수는 T번
    for day in range(T):
        #1.아침시간
        #range(N)은 0부터 N-1까지 돈다
        for i in range(N):
            for j in range(N):
                B[i][j] += 1
        #2.점심시간
        visited = [[False] * N for _ in range(N)]
        #저녁시간에 전파할 대표자 좌표 저장
        leaders = []
        #보드를 살펴본다.
        for i in range (N):
            for j in range (N):
                #이미 다른 그룹에 들어간 칸이면 건너뜀
                if visited[i][j]:
                    continue
                #(i, j)에서 BFS시작
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                group = []
                #대표자를 따로 모아두면 편함.
                # 그룹 기준 음식
                food = F[i][j]

                while queue:
                    r, c = queue.popleft()
                    #현재 같은 칸은 같은 음식 그룹에 포합됨 (중요)
                    group.append((r, c))

                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        if visited[nr][nc] == True:
                            continue
                        if F[nr][nc] != food:
                            continue
                        #음식이 같고 연결되어있으면 같은 그룹
                        queue.append((nr, nc))
                        visited[nr][nc] = True

                # 그룹이 정해지면
                #신앙심이 가장 큰 사람
                # 신앙심 가장 큰 사람 구하니까 -1부터 시작.
                INF = float('inf')
                sincere = -1
                smallest_r = INF
                smallest_c = INF
                for r, c in group:
                    ## 신앙심이 더 크면 대표자를 현재 학생으로 교체
                    if B[r][c] > sincere:
                        sincere = B[r][c]
                        smallest_r = r
                        smallest_c = c
                    #2순위 r이 작은 사람# 신앙심이 같고 r이 더 작으면 대표자를 현재 학생으로 교체
                    elif B[r][c] == sincere and r < smallest_r:
                        smallest_r = r
                        smallest_c = c
                    #3순위 신앙심도 같고 r도 같으면 c가 작은 사람# 신앙심이 같고 r도 같고 c가 더 작으면 대표자를 현재 학생으로 교체
                    elif B[r][c] == sincere and r == smallest_r and c < smallest_c:
                        smallest_c = c

                #대표자 좌표
                rep_r = smallest_r
                rep_c = smallest_c
                #대표자는 그룹원 수 -1만큼 받는다.
                B[rep_r][rep_c] += len(group) -1
                #대표자를 제외한 그룹원은 각자 신앙심을 1씩 대표자에게 넘김. 대표자의 신앙심은
                #그룹원수 -1만큼 추가되고, 나머지 그룹원은 1씩 감소함
                for r, c in group:
                    #대표자이면
                    if r == rep_r and c == rep_c:
                        continue
                    #그외는 -1씩 잃는다.
                    B[r][c] -= 1
                #이그룹의 대표자를 저장
                leaders.append((rep_r, rep_c))
        #3. 저녁시간
        #food_rank를 기준으로 대표자 좌표 리스트를 대표자의 음식 전파 순서대로 정렬하는 코드
        # 1. 대표자 신앙심 B 큰 순
        # 3. 대표자 r 작은 순
        # 4. 대표자 c 작은 순
        leaders.sort(key=lambda leader: (
            food_rank(F[leader[0]][leader[1]]),
            -B[leader[0]][leader[1]],
            leader[0],
            leader[1]
        ))
        direction = {
            0: (-1, 0),  # 상
            1: (1, 0),  # 하
            2: (0, -1),  # 좌
            3: (0, 1),  # 우
        }
        #오늘 전파를 당한 학생 표시
        defended = [[False] * N for _ in range(N)]

        for leader in leaders:
            r, c = leader
            # 오늘 저녁에 전파를 당한 대표자는 전파자 역할을 못 함
            if defended[r][c]:
                continue
            #전파자 음식
            spread_food = F[r][c]
            # 전파자의 기존 신앙심으로 방향과 간절함 계산
            direction_way = B[r][c] % 4
            x = B[r][c] -1
            #대표자는 신앙심 1만 남김
            B[r][c] = 1
            dr, dc = direction[direction_way]
            #현재 전파 위치
            cur_r = r
            cur_c = c
            # x가 0이되면 전파를 멈춤
            while x > 0:
                nr = cur_r +dr
                nc = cur_c +dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    #전파를 아예 종료하는거라서 continue가 아님
                    break
                if F[nr][nc] == spread_food:
                    cur_r = nr
                    cur_c = nc
                    continue
                #다른 음식이면 전파 발생
                defended[nr][nc] = True
                #전파 대상의 신앙심
                y = B[nr][nc]
                #강한 전파
                if x > y:
                    #전파자는 간절함이 (y+1)만큼 깎이고
                    x -= y +1
                    # 전파대상은 신앙심이 1증가함.
                    B[nr][nc] += 1
                    F[nr][nc] = spread_food

                    cur_r = nr
                    cur_c = nc
                    continue

                # 약한전파
                else:
                    B[nr][nc] += x
                    F[nr][nc] = merge_food(F[nr][nc], spread_food)
                    x = 0
                    break

            # 저녁시간 끝난 직후

        score = {
            "TCM": 0,  # 민트초코우유
            "TC": 0,  # 민트초코
            "TM": 0,  # 민트우유
            "CM": 0,  # 초코우유
            "M": 0,  # 우유
            "C": 0,  # 초코
            "T": 0,  # 민트
        }
        for i in range(N):
            for j in range(N):
                food = F[i][j]
                score[food] += B[i][j]
        print(
            score["TCM"],
            score["TC"],
            score["TM"],
            score["CM"],
            score["M"],
            score["C"],
            score["T"]
        )



solution()