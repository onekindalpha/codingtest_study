# 아파트가 일렬로 쭉 서있습니다.
# 이미  기지국이 설치된 아파트가 있습니다.
# 전파가 안 닿는 구간을 찾아서 커버해야 합니다.
# N이 엄청 큽니다.
# 5g기지국 최소로 설치하면서 , 모든 아파트에 전파를 전달
# 아파트의 개수 n
# len(n)
# # 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations
# stations는 오름차순. n보다 같거나 작은 자연수.
# # 배열에서 하나씩 꺼낼때


# 그리디, 구간계산
# # 전파의 도달 거리 W(양쪽으로 도달할 수 있음)
# 2W
# # 기지국 하나가 덮을 수 있는 구간 개수
# cover_length = 2W+1
# 아직 확인하지 않은 아파트 번호
# current_position = 1
# 만약 아직 전파구간으로 덮히지 않았다면 빈 구간 길이로 합산
# 기존 기지국만 하나씩 볼 것임.

def solution(n, stations, w):
    cover_length = 2 * w + 1
    result = 0

    current_position = 1
    # 기지국을 확인
    for station in stations:
        covered_start = station - w
        covered_end = station + w

        if current_position < covered_start:
            empty_length = covered_start -current_position
            # 새로 설치해야 하는 기지국 개수는
            # 빈 구간 길이를 기지국 하나가 덮는 길이로 나누는데
            # 조금이라도 남으면 기지국 하나를 더 설치한다.
            # 나머지가 있는 경우 몫을 하나 더하도록
            result += (empty_length + cover_length -1) // cover_length

        # 확인할 포지션은 전파 끝구간에서 다시 하나 더함
        current_position = covered_end +1
    # 기지국 뒤에까지 확인
    if current_position <=n:
        empty_length = n - current_position +1
        result += (empty_length + cover_length -1) // cover_length
    return result

print(solution(11, [4,11], 1))
# 3

print(solution(16, [9], 2))
#3