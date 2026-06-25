# n행 n열 크기의 비어있는 2차원 배열을 만듦. n이 최대 10^7이라서 nxn 배열을 만들면 메모리 초과
# 배열을 실제로 만들ㅁ면 안됨.

# 1행 1열부터 i행 i열까지의 모든 빈 칸을 숫자 i로 채우움
# 배열 값의 규칙을 만ㄷ름.
# arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지움

def solution(n, left, right):
    answer = []
    # 필요한 번호를 하나씩 봄.
    for idx in range(left, right +1):
        # 몇번째 줄에 있는지
        row = idx //n
        # 몇번째 칸인지
        col = idx % n
        # 그 칸에 들어갈 숫자.
        value = max(row, col) +1
        answer.append(value)
    return answer

print(solution(3, 2, 5))
# [3,2,2,3]
print(solution(4, 7, 14))
# [4, 3, 3, 3, 4, 4, 4, 4]
