# 스티커 n개. 1이상임.
# 원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어
# 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니
# 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다
# 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return
#  배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.
# sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.
# 양쪽으로 인접한 값을 고르면 안되는 dp 최댓값
def solution(sticker):
    sticker_count = len(sticker)
    # 스티커가 1개 또는 2개면 DP까지 갈 필요 없음# 작은 입력예외처리
    if sticker_count <= 2:
        return max(sticker)

    def cut_sticker(line_sticker):
        line_sticker_count = len(line_sticker)

        # dp라는 메모장을 실제로 만들기
        dp = [0] * line_sticker_count
        dp[0] = line_sticker[0]
        # 첫번째를 뜯었으면 다음 스티커를 뜯지 못함.
        dp[1] = max(line_sticker[0], line_sticker[1])

        # 반복문 처리
        for i in range(2, line_sticker_count):
            # 현재 스티커 점수 + 직전 x2 점수
            # 직전까지의 점수
            dp[i] = max(dp[i - 1], dp[i-2] + line_sticker[i])
        # 마지막 집까지 다 돌았을때 파이썬 인덱스는 -1이니까. (0부터 세서)
        return dp[line_sticker_count -1]

    case_without_last_sticker = cut_sticker(sticker[:-1])
    case_without_first_sticker = cut_sticker(sticker[1:])

    return max(case_without_last_sticker, case_without_first_sticker)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
# 36

print(solution([1, 3, 2, 5, 4]))
# 8

