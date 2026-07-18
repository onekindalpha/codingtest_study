# 레스토랑 외벽은 원형이고, 전체 둘레는 n이다.
# weak는 점검해야 하는 취약 지점들의 위치다.
# dist는 친구들이 1시간 동안 이동할 수 있는 거리 배열이다.
# dist의 길이 = 투입 가능한 친구 수

# 목표:
# 모든 weak 지점을 점검하기 위해 필요한 최소 친구 수를 구한다.
# 모든 친구를 투입해도 점검할 수 없으면 -1을 반환한다.

# 알고리즘:
# 완전탐색 + 순열 + 원형 배열 일자화

# 핵심 사고:
# 1. 원형 외벽은 10 다음에 11, 그다음 0, 1처럼 다시 돌아온다.
# 2. 이 원형 처리를 쉽게 하기 위해 weak 뒤에 weak+n 값을 붙여 일자로 펼친다.
# 3. 결과가 달라지는 변수는 두 가지다.
#    - 어디 취약점에서 점검을 시작하는가
#    - 어떤 친구를 먼저 투입하는가
# 4. 그래서 시작 취약점과 친구 투입 순서를 모두 시도한다.

from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)

    # 원형 배열을 일자 배열처럼 다루기 위해 weak를 확장한다.
    # 예: n=12, weak=[1,5,6,10]
    # → [1,5,6,10,13,17,18,22]
    # 여기서 13은 원래 1이 한 바퀴 돈 뒤의 위치다.
    extended_weak = weak + [w + n for w in weak]

    # 최소 친구 수를 구해야 하므로, 가능한 친구 수보다 1 큰 값으로 초기화한다.
    # 끝까지 이 값 그대로라면 모든 친구를 써도 실패했다는 뜻이다.
    answer = len(dist) + 1

    # 1. 시작 취약점을 바꿔본다.
    # weak[start]부터 점검을 시작하는 경우를 모두 시도한다.
    for start in range(weak_len):

        # 2. 친구 투입 순서를 바꿔본다.
        # 친구마다 이동 가능 거리가 다르므로, 투입 순서에 따라 결과가 달라질 수 있다.
        for friends in permutations(dist):

            # weak_idx는 아직 점검하지 못한 첫 번째 취약점의 위치를 가리킨다.
            weak_idx = start

            # 현재 경우에서 사용한 친구 수
            used_friend = 0

            # 정해진 친구 순서대로 한 명씩 투입한다.
            for friend_dist in friends:
                used_friend += 1

                # 현재 친구는 아직 점검하지 못한 취약점에서 출발한다.
                # friend_dist만큼 이동할 수 있으므로 cover_end까지 점검 가능하다.
                cover_end = extended_weak[weak_idx] + friend_dist

                # 현재 친구가 커버할 수 있는 취약점은 모두 넘긴다.
                while weak_idx < start + weak_len and extended_weak[weak_idx] <= cover_end:
                    weak_idx += 1

                # weak_len개의 취약점을 모두 넘겼다면 전체 점검 성공
                if weak_idx == start + weak_len:
                    answer = min(answer, used_friend)
                    break

    # 어떤 시작점/친구 순서로도 성공하지 못했다면 -1
    if answer == len(dist) + 1:
        return -1

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 기대값: 2

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# 기대값: 1

print(solution(12, [1, 5, 6, 10], [1, 1]))
# 기대값: -1