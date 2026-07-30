import heapq

def solution():
    # 명령의 수
    T = int(input())

    # 모든 선박의 최신 정보 저장
    # ship_info[id] = [공격력 p, 재장전 시간 r]
    ship_info = {}

    # 현재 사격 가능한 선박 id만 저장
    # 재장전 중인 선박은 여기 없어야 함
    ready_set = set()

    # 현재 사격 가능한 선박을 공격력 높은 순으로 뽑기 위한 힙
    # heapq는 작은 값이 먼저 나오므로 공격력 p는 -p로 넣음
    # (-p, id)로 넣으면
    # 1순위: p 높은 순
    # 2순위: id 작은 순
    ready_heap = []

    # 재장전 중인 선박을 복귀 시간 빠른 순으로 관리하는 힙
    # (복귀 시간, id)
    reload_heap = []

    # 각 명령은 1시간 단위로 실행됨
    # time = 현재 명령 번호
    for time in range(1, T + 1):
        work_type, *args = map(int, input().split())

        # 현재 명령을 실행하기 전에
        # 재장전이 끝난 선박들을 사격 대기 상태로 복귀시킴
        while reload_heap and reload_heap[0][0] <= time:
            ready_time, ship_id = heapq.heappop(reload_heap)

            # 이제 이 선박은 다시 사격 가능
            ready_set.add(ship_id)

            # 선박의 최신 공격력을 가져옴
            # 재장전 중에 300 명령으로 공격력이 바뀌었을 수도 있기 때문
            p = ship_info[ship_id][0]

            # 사격 가능 힙에 다시 넣음
            heapq.heappush(ready_heap, (-p, ship_id))

        # 100: 초기 선박 등록
        if work_type == 100:
            N = args[0]
            shot_ready = args[1:]

            # shot_ready는 [id, p, r, id, p, r, ...] 형태
            # 선박 1개 정보가 3칸씩 반복됨
            for i in range(0, len(shot_ready), 3):
                ship_id = shot_ready[i]
                p = shot_ready[i + 1]
                r = shot_ready[i + 2]

                # 전체 선박 정보 저장
                ship_info[ship_id] = [p, r]

                # 처음 등록된 선박은 사격 대기 상태
                ready_set.add(ship_id)

                # 공격력 높은 순으로 뽑기 위해 힙에 넣음
                heapq.heappush(ready_heap, (-p, ship_id))

        # 200: 새 선박 추가
        elif work_type == 200:
            ship_id = args[0]
            p = args[1]
            r = args[2]

            # 전체 선박 정보 저장
            ship_info[ship_id] = [p, r]

            # 새로 추가된 선박은 사격 대기 상태
            ready_set.add(ship_id)

            # 사격 가능 힙에도 추가
            heapq.heappush(ready_heap, (-p, ship_id))

        # 300: 특정 선박 공격력 변경
        elif work_type == 300:
            ship_id = args[0]
            new_p = args[1]

            # 공격력만 갱신
            # 재장전 시간 r은 그대로 유지
            ship_info[ship_id][0] = new_p

            # 현재 사격 가능한 선박이면 ready_heap에도 새 공격력으로 다시 넣음
            # 기존 공격력 기록은 힙 안에 남아 있을 수 있음
            # 나중에 꺼낼 때 최신 공격력인지 검사해서 버림
            if ship_id in ready_set:
                heapq.heappush(ready_heap, (-new_p, ship_id))

        # 400: 최대 5척 사격
        elif work_type == 400:
            p_total = 0
            ship_ids = []

            # 최대 5척만 뽑음
            while ready_heap and len(ship_ids) < 5:
                minus_p, ship_id = heapq.heappop(ready_heap)
                p = -minus_p

                # 이미 사격해서 재장전 중인 선박이면 무시
                if ship_id not in ready_set:
                    continue

                # 힙에 남아 있는 과거 공격력 기록이면 무시
                # 예: 예전 p=7 기록이 남았는데 현재 p=6이면 버림
                if ship_info[ship_id][0] != p:
                    continue

                # 최신 재장전 시간
                r = ship_info[ship_id][1]

                # 사격 참여
                p_total += p
                ship_ids.append(ship_id)

                # 사격했으므로 이제 사격 대기 상태가 아님
                ready_set.remove(ship_id)

                # 현재 time에 사격했고 r시간 뒤 다시 사격 가능
                ready_time = time + r

                # 재장전 힙에 넣음
                heapq.heappush(reload_heap, (ready_time, ship_id))

            print(p_total, len(ship_ids), *ship_ids)

solution()