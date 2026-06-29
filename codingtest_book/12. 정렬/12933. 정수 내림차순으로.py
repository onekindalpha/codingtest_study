def solution(n):
    digits = str(n)
    sorted_digits = sorted(digits, reverse=True)
    # sorted의 결과는 항상 리스트
    # join은 넣고 붙이는 메서드
    joined_digits = ''.join(digits)
    answer = int(joined_digits)
    return answer

print(solution(118372))
# 873211

print(solution(12345))
# 54321

print(solution(1000))
# 1000

print(solution(9876))
# 9876