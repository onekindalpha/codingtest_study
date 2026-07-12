# 징검다리 문제 핵심 정리
# 돌 숫자 = 그 돌을 밟을 수 있는 총 횟수
# people번째 친구 기준에서 stone < people 이면 못 밟는 돌
# 못 밟는 돌이 연속으로 k개 이상이면 건널 수 없음

# 정답은 "최대 몇 명?"이라는 숫자
# N명이 가능하면 N보다 적은 인원은 무조건 가능
# N명이 불가능하면 N보다 많은 인원은 무조건 불가능
# => 가능/불가능 경계가 생기므로 이분탐색 사용

# 풀이:
# 1. people명이 건널 수 있는지 검사한다.
# 2. 가능하면 더 큰 인원수를 탐색한다.
# 3. 불가능하면 더 작은 인원수를 탐색한다.
# 4. 가능한 최대 people 값을 반환한다.

def solution(stones, k):
    # people번째 친구가 건널 수 있는지 확인하는 함수
    def can_cross(people):
        #못밟는돌연속개수
        broken = 0
        #stone을 앞에서부터 하나씩 확인한다:
        for stone in stones:
            # people번째 친구가 이 돌을 못 밟는 경우
            if stone < people:
                broken += 1
            else:
                broken = 0
                #못밟는 돌이 k개 연속이면 건널 수 없음
            if broken >= k:
                return False
            #끝까지 했는데 k개 연속이 없으면 건널 수 있음
        return True

    #가능한 사람 수 범위
    left = 1
    right = max(stones)
    answer = 0

    #사람 수를 이분탐색
    while left <= right:
        mid = (left + right) // 2

        # mid명이 건널 수 있으면
        if can_cross(mid):
            answer = mid
            #더 많이 가능한지 확인한다.
            left = mid + 1
        #mid명이 못 건너면
        else:
            #사람수를 줄인다.
            right = mid - 1

    return answer
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

