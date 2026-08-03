def solution(A,B):
    sum = 0
    len(A) == len(B)
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        sum += (A[i] * B[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer = sum
    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))