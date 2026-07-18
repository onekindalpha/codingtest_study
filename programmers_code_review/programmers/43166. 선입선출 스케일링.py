# 처리해야 될 작업의 개수 n
# 이를 처리하기 위한, cpu 여러개의 코어가 있고, 코어별로 작업 처리 시간이 다르다.
# 각 코어의 처리시간이 담긴 배열 cores
# 마지막 작업을 처리하는 코어의 번호! 작업처리시간이 아니라.

# 이분탐색을 고민해야 할 때는,
# 1) 답이 숫자고
# 2) 답의 범위가 크고
# 3) 어떤 값 mid를 정했을때 가능 불가능을 판단할 수 있고,
# 4) mid가 커질수록 가능 상태가 유지될 때

def solution(n, cores):
    # 코어 개수
    core_count = len(cores)

    # 0초에 모든 코어가 작업을 하나씩 받는다.
    # 그래서 n(작업개수가)이 코어개수 이하이면, n번째 작업은 n번째 코어가 받는다.
    if n <= core_count:
        return n

    # 0초에 이미 core_count개의 작업은 배정되었으므로
    # 앞으로 추가로 배정해야 하는 작업 개수만 남긴다.
    n -= core_count

    # 이분탐색으로 찾을 대상은 코어 번호가 아니라 시간이다.
    left = 0

    # 가장 빠른 코어가 남은 n개의 작업을 전부 처리한다고 생각한 안전한 최대 시간
    right = min(cores) * n

    # n번째 작업이 배정되는 최소 시간을 찾는다.
    while left < right:
        mid = (left + right) // 2

        # mid 시간까지 추가로 배정된 작업 수
        # 각 코어는 mid // core 만큼 추가 작업을 받을 수 있다.
        assigned = sum(mid // core for core in cores)

        # mid 시간까지 남은 n개 이상 배정 가능하다면
        # mid는 충분한 시간이므로
        # mid보다 더 빠른 시간이 있는지 왼쪽을 본다.
        if assigned >= n:
            right = mid

        # mid시간까지 n개 배정이 어렵다.
        # 고로 mid 이후를 찾아본다.
        else:
            left = mid + 1

    # 여기부터 while문 끝난 후
    time = left

    # time - 1 시간까지 이미 추가 배정된 작업 수
    count = sum((time - 1) // core for core in cores)

    # time시점에 비는 코어들을 앞번호부터 확인
    for i, core in enumerate(cores):
        # 비는 코어를 만나면
        if time % core == 0:
            # 새 작업 하나가 배정된다.
            count += 1

            # 그 개수가 n이 되는 순간. 멈춘다. 파이썬 인덱스 고려 +1
            if count == n:
                return i + 1