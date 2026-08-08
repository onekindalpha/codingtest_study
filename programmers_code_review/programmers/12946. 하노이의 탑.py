def hanoi(n, start, end, mid, answer):
    if n == 1:
        answer.append([start, end])
        return
    # n이 1이 아닐때
    hanoi(n-1, start, mid, end, answer)
    # 처음에서 끝으로 옮긴다.
    answer.append([start, end])
    hanoi(n-1, mid, end, start, answer)
    return answer
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

print(solution(2))