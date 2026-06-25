# 제한 시간 limit 안에 모든 퍼즐을 풀 수 있는 최소 숙련도 level을 구한다.
# 퍼즐의 난이도 diff, 현재 퍼즐의 소요 시간 time_cur, 이전 퍼즐의 소요시간 time_prev, 나의 숙련도 level
# diff <= level 이면 퍼즐을 틀리지 않고 time_cur만큼의 시간을 사용하여 해결함.
# diff > level이면 퍼즐을 diff - level 번 틀림. 퍼즐을 틀릴 때마다, time_cur만큼의 시간을 사용하여, time_prev 만큼의 시간을 사용해 이전 퍼즐을 다시 풀고 와야 함.
# 이전 퍼즐은 항상 맞춤. diff - level번 틀린 이후에 다시 퍼즐을 풀면 time_cur만큼의 시간을 사용하여 퍼즐을 해결함.
# 퍼즐 게임에는 전체 제한 시간 limit이 정해져 있음. limit의 최솟값. 모든 난이도, 소요 시간은 양의 정수.
# 퍼즐의 난이도 순서대로 담은 1차원 정수 배열 diffs, 퍼즐의 소요 시간 순서대로 담은 1차원 정수 배열 times, 전체 제한 시간 limit
# 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값 정수 return
# level로 풀 수 있는지.
def solution(diffs, times, limit):
    # 함수에 level을 하나씩 넣어보.ㅁ
    def can_solve(level):
        # 퍼즐의 난이도.
        total = 0
        for i in range(len(diffs)):
            # 지금 i번째 퍼즐의 난이도와 소요 시간을 꺼냄.
            diff = diffs[i]
            # 현재 퍼즐의 소요시간
            time_cur = times[i]
            # 내 숙련도가 충분하면 안 틀리고 현재 퍼즐 시간만 더한다.
            if diff <= level:
                total += time_cur
            # 숙련도가 부족하면 틀린 횟수만큼 현재 퍼즐 + 이전 퍼즐 시간을 더하고, 마지막 성공 시간도 더한다.
            # diff > level이면 diff -level번 틀린다. 틀릴 때마다 time_cur+time_prev만큼의 시간이 든다.
            # 다 틀린 후, 마지막에 풀어서, time_cur시간이 든다.
            else:
                # wrong은 현재 퍼즐을 틀리는 횟수임. 이전 퍼즐은 틀리지 않는다.
                wrong = diff - level
                time_prev = times[i -1]
                total += wrong * (time_cur + time_prev) + time_cur

    #    print("level", level, "일 때 총 시간:", total)
        return total <= limit

    # 처음으로 제한시간으로 풀 수 있는 Level을 발견하면 그게 정답이다.
    # 이진탐색으로 바꾸기. level이 커질수록 단조증가하니까. 처음가능한 level찾기 위해서임.
    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_solve(mid):
            answer = mid
            right = mid -1
        else:
            left = mid +1
    return answer

print(solution([1,5,3], [2,4,7], 30))
# 3

print(solution([1,4,4,2], [6, 3, 8, 2], 59))
# 2