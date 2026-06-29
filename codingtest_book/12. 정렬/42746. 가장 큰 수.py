def solution(numbers):
    str_numbers = list(map(str, numbers))

    str_numbers.sort(key=lambda x: x*4, reverse=True)

    answer = "".join(str_numbers)

    if answer[0] == "0":
        return "0"
    return answer

print(solution([6, 10, 2]))
# 6210

print(solution([3, 30, 34, 5, 9]))
# 9534330

print(solution([0, 0, 0]))
# 0