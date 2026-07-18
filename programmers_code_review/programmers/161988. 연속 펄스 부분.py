# 펄스 수열이란 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열임
# 연속부분 수열에 같은 길이의 펄스 수열을 각 원소끼리 곱해
# 연속 펄스 부분 수열을 만들려고 함
# sequence가 수열로 주어짐
# 연속 펄스 부분 수열의 합 중 가장 큰 것
# 연속 부분 수열이란, 원래 수열에서 연속으로 붙어 있는 일부를 고른 거

# 일단 합이 최대가 되어야 하니까.
# 연속 부분 수열과 펄스 수열 길이는 같다.
# 펄스는 1, -1이 번갈아 나온다.
# 합의 최댓값을 구한다.
#
# dp[i] = i번째 원소를 반드시 포함하고,
#         i번째 원소에서 끝나는 연속 부분 수열 합의 최댓값

def solution(sequence):
    #sequence = [2, 3, -6, 1, 3, -1, 2, 4]
    n = len(sequence)
    # case 1
    pulse1 = ([1, -1]* ((n +1)//2))[:n]
    # case 2
    pulse2 = ([-1, 1]* ((n +1)//2))[:n]
    #완성 배열
    #case 1
    arr1 = []
    #case 2
    arr2 = []
    for i in range(n):
        arr1.append(sequence[i] * pulse1[i])
        arr2.append(sequence[i] * pulse2[i])
    # 연속합 최댓값 구하기.
    # 연속합 적용 원리는 DP
    # 1. i번째 숫자부터 새로 시작한다
    # 2. 앞에서 이어진 연속합에 i번째 숫자를 붙인다
    # cur = 현재 숫자에서 끝나는 연속합 최댓값
    # best = 지금까지 나온 연속합 최댓값
    def max_sum(arr):
        cur = arr[0]
        best = arr[0]

        for num in arr[1:]:
            #1. num부터 새로 시작한다.
            #2. 앞에서 이어진 연속합 cur에 num을 붙인다.
            # 둘 중 큰 값을 cur로 갱신한다.
            cur = max(num, cur + num)
            # 전체 연속합 최댓값을 갱신한다.
            best = max(best, cur)
        return best
    # 두배열에 연속합 최댓값을 찾는 함수를 적용한다.
    answer1 = max_sum(arr1)
    answer2 = max_sum(arr2)

    return max(answer1, answer2)

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
# 10