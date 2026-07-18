# N행 4열
# land는 2차원 배열
# 한 행씩 내려올 때 같은 열을 연속해서 밟을 수 없음
# 마지막 행까지 모두 내려왔을때 얻을 수 있는 점수의 최대값
# # 현재칸 점수는 이전 행의 다른 열의 최댓값
# land[y][x] = y행 x열까지 왔을 때 최대 누적 점수
def solution(land):
    row = len(land)
    # 행, 전체 행을 반복하면서,
    for y in range(1, row):
        land[y][0] += max(land[y-1][1], land[y-1][2], land[y-1][3])
        land[y][1] += max(land[y-1][0], land[y-1][2], land[y-1][3])
        land[y][2] += max(land[y-1][0], land[y-1][1], land[y-1][3])
        land[y][3] += max(land[y-1][0], land[y-1][1], land[y-1][2])
    # 마지막 행에 저장된 누적 점수들 중 최댓값을 반환한다.
    return max(land[-1])

print(solution([
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [4, 3, 2, 1]
]))  # 16