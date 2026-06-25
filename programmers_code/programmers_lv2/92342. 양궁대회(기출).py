# 어피치가 이미 n발을 모두 쏜 상태이고, 이제 라이언이 n발을 쏜다.
# info[i]는 어피치가 10-i점에 맞힌 화살 개수이다.
# 예: info[0] = 10점 화살 수, info[10] = 0점 화살 수
#
# 라이언도 길이 11짜리 배열 ryan을 만든다.
# ryan[i]는 라이언이 10-i점에 맞힌 화살 개수이다.
#
# 각 점수 칸마다 라이언의 선택은 크게 두 가지다.
# 1. 이 점수 칸을 가져간다:
#    어피치보다 1발 더 많이 쏴야 하므로 info[i] + 1발 필요
# 2. 이 점수 칸을 포기한다:
#    0발 쏜다
#
# 10점부터 0점까지 각 칸에 대해
# "가져갈지 / 포기할지"를 DFS로 모두 시도한다.
#
# 모든 경우를 확인한 뒤,
# 라이언 점수 - 어피치 점수 차이가 가장 큰 배열을 답으로 고른다.
# 단, 점수 차이가 같다면 더 낮은 점수에 화살을 많이 쏜 배열을 고른다.
# 라이언이 이기는 경우가 하나도 없으면 [-1]을 반환한다.

def solution(n, info):
    answer = [-1]
    max_gap = 0
    # 라이언의 답안
    ryan = [0] * 11

    def dfs(idx, arrows_left):
        print("지금보는칸:", idx, "점수:", 10-idx, "남은 화살:", arrows_left)

        if idx == 11:
            print("끝까지 옴", ryan)
            return
        # 라이언이 이기는 데 필요한 화살수
        need = info[idx] +1
        # info[idx]는 어피치가 지금 보고 있는 점수 칸에 몇 발을 맞혔는지
        # 남은 화살이 충분할 때, 현재 점수 칸을 라이언이 가져가는 선택을 해봄.
        if arrows_left >= need:
            # 라이언이 현재 칸에 필요한 만큼 화살을 넣는다.
            ryan[idx] = need
            # 현재 칸 끝났으니까 다음 칸으로 가자. 이렇게 끝까지 가봄.
            dfs(idx + 1, arrows_left - need)
            # 방금 해본 선택을 취소해봄
            ryan[idx] = 0# 어피치가 이미 n발을 모두 쏜 상태이고, 이제 라이언이 n발을 쏜다.
# info[i]는 어피치가 10-i점에 맞힌 화살 개수이다.
# 예: info[0] = 10점 화살 수, info[10] = 0점 화살 수
#
# 라이언도 길이 11짜리 배열 ryan을 만든다.
# ryan[i]는 라이언이 10-i점에 맞힌 화살 개수이다.
#
# 각 점수 칸마다 라이언의 선택은 크게 두 가지다.
# 1. 이 점수 칸을 가져간다:
#    어피치보다 1발 더 많이 쏴야 하므로 info[i] + 1발 필요
# 2. 이 점수 칸을 포기한다:
#    0발 쏜다
#
# 10점부터 0점까지 각 칸에 대해
# "가져갈지 / 포기할지"를 DFS로 모두 시도한다.
#
# 모든 경우를 확인한 뒤,
# 라이언 점수 - 어피치 점수 차이가 가장 큰 배열을 답으로 고른다.
# 단, 점수 차이가 같다면 더 낮은 점수에 화살을 많이 쏜 배열을 고른다.
# 라이언이 이기는 경우가 하나도 없으면 [-1]을 반환한다.

def solution(n, info):
    answer = [-1]
    max_gap = 0

    # 라이언의 답안
    ryan = [0] * 11

    # 점수 차이 계산 함수
    def calc_gap():
        apeach_score = 0
        ryan_score = 0

        for i in range(11):
            score = 10 - i

            if ryan[i] > info[i]:
                ryan_score += score
            elif info[i] > 0:
                apeach_score += score

        return ryan_score - apeach_score

    # 점수 차이가 같을 때, 더 낮은 점수에 많이 쏜 답인지 비교
    def is_better(candidate, current):
        if current == [-1]:
            return True

        # 0점부터 비교해야 하므로 뒤에서 앞으로 본다
        for i in range(10, -1, -1):
            if candidate[i] > current[i]:
                return True
            elif candidate[i] < current[i]:
                return False

        return False

    def dfs(idx, arrows_left):
        nonlocal answer, max_gap

        # idx == 10은 0점 칸
        # 남은 화살을 전부 0점에 넣고 점수 계산
        if idx == 10:
            ryan[10] = arrows_left

            gap = calc_gap()

            if gap > max_gap:
                max_gap = gap
                answer = ryan[:]

            elif gap == max_gap and gap > 0:
                if is_better(ryan, answer):
                    answer = ryan[:]

            ryan[10] = 0
            return

        # 라이언이 현재 점수 칸을 가져가는 데 필요한 화살 수
        need = info[idx] + 1

        # 선택 1: 현재 점수 칸을 라이언이 가져가는 경우
        if arrows_left >= need:
            ryan[idx] = need
            dfs(idx + 1, arrows_left - need)
            ryan[idx] = 0

        # 선택 2: 현재 점수 칸을 포기하는 경우
        ryan[idx] = 0
        dfs(idx + 1, arrows_left)

    # 10점 칸부터 시작
    dfs(0, n)

    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))