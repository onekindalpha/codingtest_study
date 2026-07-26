# 고정길이 큐 시뮬레이션
# 왼쪽에서 빼고, 오른쪽에 넣는 작업이 반복되면 deque를 쓴다.LIFO이 아니라 첫번째넣은게 먼저 나감 FIFO
# 초세라는 게 핵심인걸 놓쳤음
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time= 0
    bridge = deque([0] * bridge_length)
    #현재 다리에 오른 무게
    current_bridge_weight = 0
    #맨 앞 대기 트럭 하나를 계속 확인해야 하니까 큐로 바꿈
    #왼쪽에서 자주 빼야 하면 deque로 바꾼다. 대기열이라는 것을 잊지마.
    trucks = deque(truck_weights)
    #대기트럭이 아직 남아있거나, 다리 위해 트럭이 아직 있으면,
    while trucks or current_bridge_weight >0:
        # 1. bridge 왼쪽에서 하나 뺀다
        out = bridge.popleft()
        # 2. 빠진 값만큼 현재 다리 무게에서 뺀다
        current_bridge_weight -= out
        # 3. 다음 트럭을 올릴 수 있으면 오른쪽에 트럭 무게 추가
        # 대기 트럭이 남아있고, 현재 다리 위 무게에서 대기열에 올라가있어서, 다음에 올릴 트럭무게가 다리 최대 허용무게를 넘지 않으면
        if trucks and current_bridge_weight + trucks[0] <= weight:
            # 대기열에서 트럭을 꺼냄
            truck = trucks.popleft()
            bridge.append(truck)
            current_bridge_weight += truck
        # 4. 못 올리면 오른쪽에 0 추가
        else:
            bridge.append(0)
        # 5. time += 1
        time +=1
    return time
    # 다리에 올라탈 수 있는 트럭 수 최대 bridge_length대
    # 다리가 건딜 수 있는 무게 weight이하 (다리에 오른 트럭 무게만 고려)
    # 다리를 건너는 트럭의 무게는 다리가 견딜 수 있는 무게 이하일때,
    # 트럭별 무게 = 순서대로 최단시간 안에 다리를 건너려면.
    # 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지

