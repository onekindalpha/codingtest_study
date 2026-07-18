# 일렬로 나열된 n개의 집
# 트럭에는 재활용 택배 상자를 최대 cap개 실을 수 있음
# 각 집마다 배달할 재활용 택배 상자 개수와 수거할 빈 재활용 택배 상자의 개수를 알고 있을 때
# 트럭하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
# 각 집에 배달 및 수거할 때 원하는 개수만큼 택배를 배달 및 수거 가능함

# 트럭에 실을 수 있는 재활용 택배 상자의 최대 개수 cap
# 배달할 집의 개수를 나타내는 정수 n
# 배달할 재활용 택배 상자의 개수를 담은 1차원 정수 배열 deliveries
# 각 집에서 수거할 빈 재활용 택배 상자의 개수를 담은 1차원 정수 배열 pickups

# 트럭 하나로 모든 배달과 수거를 마치고 물류 창고까지 돌아올 수 있는 최소 이동 거리

def solution(cap, n, deliveries, pickups):
    answer = 0
    # 아직 배달할게 남은 가장 먼집
    # 파이썬 인덱스는 0부터 시작하므로.
    d = n -1
    # 아직 수거할게 남은 가장 먼집
    # 파이썬 인덱스는 0부터 시작하므로.
    p = n -1
    # 반복
    # d가 가리키는 집에 배달할 게 없으면, 왼쪽 집으로 한 칸 옮겨라.
    # d를 왼쪽으로 옮기면서 배달 0인 집은 건너 뛴다.
    while d>=0 or p >= 0:
        while d >= 0 and deliveries[d] == 0:
            d -=1
        #p를 왼쪽으로 옮기면서 수거 0인 집은 건너뛴다.
        while p >= 0 and pickups[p] == 0:
            p -= 1
        # 둘다 더 이상 처리할 집이 없으면 끝낸다.
        if d <0 and p <0:
            break

            # 이번에 가야 하야 하는 가장 먼집 = max(d, p)
        farthest = max(d, p)

            # 왕복 거리 answer에 더한다.
        #파이썬 인덱스를 고려하여 1을 더한다.
        answer += (farthest + 1) * 2
            # 배달 cap개를 먼집부터 줄인다.
        # box는 이번 왕복에서 아직 처리할 수 있는 남은 용량이다.
        remain_delivery_cap = cap
        # 먼집 부터 box가 0이 될 때까지
        while d>= 0 and remain_delivery_cap >0:
            # 현재 d번 집에 배달해야 할 양이 트럭에 남은 배달 가능량보다 작거나 같으면
            if deliveries[d] <= remain_delivery_cap:
                remain_delivery_cap -= deliveries[d]
                # 배달해야할 양은 0이 됨.
                deliveries[d] = 0
                d -=1
            else:
                # 현재 배달해야 할 양보다 이번 트럭에 남은 배달 가능 용량보다 많음.
                deliveries[d] -= remain_delivery_cap
                # 남은 배달 가능 용량은 0임.
                remain_delivery_cap = 0
            # 수거 cap개를 먼집부터 줄인다.
        remain_pickup_cap = cap
        # 먼집 부터 remain_delivery_cap가 0이 될 때까지
        while p >= 0 and remain_pickup_cap > 0:
            # 현재 p번 집에서 수거해야 할 양을 이번에 다 할 수 있다면,
            if pickups[p] <= remain_pickup_cap:
                remain_pickup_cap -= pickups[p]
                # 수거해야 할 양은 0이 됨.
                pickups[p] = 0
                p -= 1
            else:
                # 현재 수거해야 할 양이 이번 트럭에 남은 수거 가능 용량보다 많음.
                pickups[p] -= remain_pickup_cap
                # 그럼 남은 수거 가능 용량은 0임.
                remain_pickup_cap = 0

    return answer
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# 16

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
# 30

print(solution(3, 3, [0, 0, 0], [0, 0, 0]))
# 0

print(solution(2, 3, [0, 0, 1], [0, 0, 0]))
# 6

print(solution(2, 3, [0, 0, 0], [0, 0, 1]))
# 6