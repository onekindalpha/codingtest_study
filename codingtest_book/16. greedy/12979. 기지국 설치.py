# 유형: 그리디
# 아파트는 1번부터 N번까지 일렬로 놓여 있다.
# 기지국 하나는 현재 위치 기준 왼쪽 W칸, 오른쪽 W칸까지 덮는다.
# 즉 기지국 하나가 덮는 범위는 2 * W + 1이다.
# 기존 기지국이 덮는 구간은 건너뛴다.
# 전파가 안 닿는 가장 왼쪽 아파트를 만나면,
# 그 아파트를 덮을 수 있는 가장 오른쪽 위치에 새 기지국을 설치한다.
# 그렇게 해야 한 번 설치로 오른쪽을 최대한 많이 덮을 수 있다.
# 그래서 왼쪽부터 순서대로 보며 최소 설치 개수를 구하는 그리디 문제다.

def solution(N, stations, W):
    answer = 0
    location = 1
    idx = 0
    while location <= N:
        # 아직 확인할 기존 기지국이 남아 있고,
        # 지금 location이 그 기지국의 전파 시작 지점에 도달했다면
        if idx < len(stations) and location >= stations[idx] - W:
            location = stations[idx] + W + 1
            idx += 1
        else:
            location += 2 *W + 1
            answer += 1
    return answer

# 테스트 1
N = 11
stations = [4, 11]
W = 1

print(solution(N, stations, W))
# 예상 결과: 3


# 테스트 2
N = 16
stations = [9]
W = 2

print(solution(N, stations, W))
# 예상 결과: 3
