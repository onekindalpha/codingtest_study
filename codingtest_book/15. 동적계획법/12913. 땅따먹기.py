# n행 4열
# 모든 칸에는 점수.
# 1행부터 땅을 밟으며 한 행씩 내려옴. 한 칸 만 밟을 수 있음
# 같은 열을 연속해서 밟을 수 없는 특수 규칙
# 마지막 행까지 모두 내려왔을 때 얻을 수 있는 점수의 최대값 return
# 땅은 2차원 배열
# 점수는 100 이하의 자연수

def solution(land):
    for row in range(1, len(land)):
        for col in range(4):
            previous_best = 0

            for previous_col in range(4):
                if previous_col == col:
                    continue
                # 윗줄에서 올 수 있는 점수 중 제일 큰 값
                previous_best = max(previous_best, land[row-1][previous_col])

            # previous_best를 현재 칸에 더한다.
            land[row][col] += previous_best
    # 마지막 행까지 내려왔을때 최대 점수니까, 마지막 줄에서 제일 큰 값을 return
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
# 16

# dfs 완전탐색: 가능한 길을 전부 직접 걸어본다.
# dp: 각 칸까지 왔을 때의 최고 점수만 저장한다.