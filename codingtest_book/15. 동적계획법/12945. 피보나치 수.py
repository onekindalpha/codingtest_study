def solution(n):
    fib = [0, 1]

    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 1234567)
    return fib[n]

print(solution(3))  # 2
print(solution(5))  # 5
print(solution(6))  # 8