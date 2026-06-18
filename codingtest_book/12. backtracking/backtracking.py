# 중복이 없어야 함. 그래서 오름차순으로 정렬되어야 함.

def solution(n):
    answer= []

    def dfs(start, current_sum, path):
        if current_sum ==10:
            answer.append(path[:])
            return
        if current_sum > 10:
            return
        # ex. dfs([1, 0, []))
        for num in range(start, n+1):
            if current_sum + num > 10:
                break
            path.append(num)
            # 입출력 조건이 오름차순 정렬, 중복 조합이 안되므로, 더 큰 숫자를 골라서 보는 것임.
            dfs(num +1, current_sum + num, path)
            path.pop()

    dfs(1, 0, [])
    return answer

print(solution(5))

print(solution(2))

print(solution(7))

