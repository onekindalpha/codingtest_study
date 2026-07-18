def solution(arr1, arr2):

    answer = []
    for row in range(len(arr1)):
        result_row = []

        for col in range(len(arr2[0])):
            total = 0
            for k in range(len(arr2)):
                total += arr1[row][k] * arr2[k][col]
            result_row.append(total)
        answer.append(result_row)
    return answer

print(solution(
    [[1, 4], [3, 2], [4, 1]],
    [[3, 3], [3, 3]]
))
# 예상 결과: [[15, 15], [15, 15], [15, 15]]


print(solution(
    [[2, 3, 2], [4, 2, 4], [3, 1, 4]],
    [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
))
# 예상 결과: [[22, 22, 11], [36, 28, 18], [29, 20, 14]]