def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        new_array = array[i-1:j]
        sorted_array = sorted(new_array)
        selected_number = sorted_array[k-1]
        answer.append(selected_number)

    return answer

# 테스트 1
assert solution(
    [1, 5, 2, 6, 3, 7, 4],
    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
) == [5, 6, 3]

# 테스트 2: 하나만 자르는 경우
assert solution(
    [1, 5, 2, 6, 3, 7, 4],
    [[4, 4, 1]]
) == [6]

# 테스트 3: 전체 배열을 자르는 경우
assert solution(
    [1, 5, 2, 6, 3, 7, 4],
    [[1, 7, 3]]
) == [3]

# 테스트 4: 이미 정렬된 배열
assert solution(
    [1, 2, 3, 4, 5],
    [[1, 5, 5], [1, 3, 2]]
) == [5, 2]

print("모든 테스트 통과!")