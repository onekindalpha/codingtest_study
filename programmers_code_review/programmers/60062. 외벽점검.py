# weak는 오름차순으로 주어진다. 취약지점 위치가 담긴 배열 weak
# dist는 정렬되어 있다고 보장되지 않으므로 친구 순서를 모두 시도해야 한다.
# 원형 외벽은 시작점을 바꿔가며 일직선으로 펼쳐서 생각한다.
# 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동함.
# weak_extended = weak + [w + n for w in weak]
# 각 시작점마다 친구 순열(순서를 바꿔서 줄 세우는 것)을 적용해, 현재 친구가 덮지 못하는 취약점이 나오면 다음 친구를 투입한다.
# 모든 취약점을 덮는 데 필요한 친구 수의 최솟값을 반환한다.
# 1) 시작점을 바꿔본다 2) 친구 순서를 바꿔본다. 3) 취약점을 앞에서부터 다 점검할 수 있는지 본다.
# n은 외벽의 길이, dist 친구의 이동가능거리 배열.
# 순열 in python
from itertools import permutations

def solution(n, weak, dist):
    # 취약한 지점의 개수
    weak_len = len(weak)

    # 0. 원형을 일직선으로 펴기
    weak_extended = weak[:]

    for w in weak:
        weak_extended.append(w + n)

    # 친구 수 최솟값 후보
    answer = len(dist) + 1

    # 1. 시작점을 바꿔보기
    for start in range(weak_len):

        # 2. 친구 이동 가능 거리 순서를 모두 바꿔보기
        for friends in permutations(dist):

            # 이번 순서에서 첫 번째 친구부터 사용
            friend_idx = 0

            # 첫 번째 친구가 점검 가능한 끝 위치
            cover_end = weak_extended[start] + friends[friend_idx]

            # 일단 성공한다고 가정
            success = True

            # 3. 이번 시작점 기준으로 취약점 weak_len개 확인
            for i in range(start, start + weak_len):

                # 현재 친구가 이 취약점까지 못 가면
                if weak_extended[i] > cover_end:
                    # 다음 친구 투입
                    friend_idx += 1

                    # 더 이상 보낼 친구가 없으면 실패
                    if friend_idx == len(friends):
                        success = False
                        break

                    # 다음 친구를 현재 못 점검한 취약점에서 출발시킴
                    cover_end = weak_extended[i] + friends[friend_idx]

            # 모든 취약점을 점검했다면 최소 친구 수 갱신
            if success:
                answer = min(answer, friend_idx + 1)

    # 끝까지 봤는데 answer가 안 바뀌었으면 불가능
    if answer == len(dist) + 1:
        return -1

    return answer


print(solution(12, [1,5,6,10], [1,2,3,4]))
# 2

print(solution(12, [1,3,4,9,10], [3,5,7]))
# 1
