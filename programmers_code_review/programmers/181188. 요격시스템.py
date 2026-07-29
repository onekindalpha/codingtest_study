# 일단 최대한 겹치는 범위에 쏴야할 듯
# targets = [s, e]
# 요격미사일은 s나 e에서는 못쏨.
# target의 길이라던가, s,e의 값이 클 수 잇어 보임
# 정렬을 쓰려면 lambda를 써야함.
# 요격 미사일은 실수인 x좌표에서도 발사할 수 있음.
# e의 최솟값부터 쏴야함.
# 그래서 e 오름차순 정렬 후, 이전 shot으로 못 맞히는 구간이 나오면 새로 쏜다.

def solution(targets):
    # e기준 오름차순 정렬.
    sorted_targets = sorted(targets, key=lambda x: x[1])
    answer = 0
    #최솟값을 구해야 하니까
    shot = -1
    for target in sorted_targets:
        s = target[0]
        e = target[1]
        # 현재 s시작점이 기존 쏜 shot보다 같거나 크면. 다시 쏴야함.
        if s >= shot:
            answer +=1
            # shot은 실제 x좌표가 아니라 e보다 작은 실수에 쐈다는 표시값임
            shot = e

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))