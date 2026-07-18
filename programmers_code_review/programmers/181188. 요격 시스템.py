# 정수 쌍(s, e)형태
# targets: 각 폭격 미사일의 x좌표 범위 목록
# 특정 x좌표에 걸쳐있는 모든 폭격 미사일을 관통하여 한번에 요격할 수 있다.
# (s, e)로 표현되는 폭격 미사일은 s와 e에서 발사하는 요격 미사일로는 요격할 수 없다.
# 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값

# 현재 미사일의 시작점이 이전 발사 위치보다 오른쪽이거나 같으면 이전 발사로는 못 맞춘다.

def solution(targets):
    # 끝점 기준으로 target을 정렬하기.
    targets.sort(key=lambda target: target[1])
    # 답은 요격 미사일 수
    answer = 0
    # 이전에 요격 미사일을 쏜 위치
    shoot = None
    for start, end in targets:
        # 아직 쏜적이 없거나,
        # 이전 요격 위치로 현재 미사일을 맞출 수 없으면 새로 쏜다.
        if shoot is None or start >= shoot:
            # 요격 미사일을 새로 쏜다.
            answer += 1
            # 이번 요격 위치의 기준을 현재 구간의 end로 갱신한다.
            shoot = end
    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
# 3

print(solution([[1, 4], [2, 5], [3, 6]]))
# 1

print(solution([[1, 4], [4, 5]]))
# 2

print(solution([[1, 3], [3, 5], [5, 7]]))
# 3

print(solution([[1, 10], [2, 9], [3, 8], [4, 7]]))
# 1