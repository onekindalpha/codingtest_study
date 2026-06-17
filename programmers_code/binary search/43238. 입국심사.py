# 최단거리 탐색 문제가 아니다.
# 사람을 한 명씩 심사대에 배치하면 n이 너무 커서 시간 초과가 난다.
# 따라서 "시간 X분 안에 몇 명을 처리할 수 있는가?"로 문제를 바꿔야 한다.
# 특정 시간 안에 처리 가능한 사람 수를 계산하고,
# n명 이상 처리 가능하면 시간을 줄이고,
# 부족하면 시간을 늘리는 이분탐색 문제다.
#
# 1. 최소 시간 left를 정한다.
# 2. 최대 시간 right를 정한다.
# 3. left와 right의 가운데 시간 mid를 구한다.
# 4. mid분 동안 총 몇 명을 처리할 수 있는지 계산한다.
# 5. 처리 가능 인원이 n명 이상이면:
#    - mid는 가능한 시간이다.
#    - 하지만 더 줄일 수 있는지 확인한다.
# 6. 처리 가능 인원이 n명보다 적으면:
#    - mid는 부족한 시간이다.
#    - 시간을 늘린다.
# 7. 가능한 시간 중 가장 작은 값을 return한다.

def solution(n, times):
    # 심사대 수는 times의 길이만큼 주어진다.
    # 각 심사관마다 한 명을 심사하는 데 걸리는 시간이 다르다.
    # 각 심시관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times. -> times 안의 값 한나는 심사관 한 명의 심사 시간.
    # ex. times = [7, 10] , 구하는 건 ex. X = 28 -> answer변수로.
    answer = 0
    # 최소시간
    left = 1
    # 최대시간
    right = max(times) *n

    while left <= right:
        mid = (left + right) // 2

        people = 0
        for time in times:
            people += mid // time

        if people >=n:
            answer = mid
            # 최소시간을 찾기 위해 왼쪽으로 약간 줄여봄.
            right = mid -1
        else:
            # mid분 안에는 사람을 다 처리 못하므로 시간을 조금 늘려봄.
            left = mid +1
            pass
    return answer

print(solution(6, [7, 10]))
# 28