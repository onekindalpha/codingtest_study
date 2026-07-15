# 2차원 정수 배열 arr
# arr을 쿼드 트리와 같은 방식으로 압축
# 압축이 안될때 4등분 함.
#1. 압축하고자 하는 특정 영역 S
#2. S내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축
#3. 그렇지 않다면, S를 정확히 4개의 정사각형 영역(입출력 예를 참고)으로 쪼갠 후 각 정사각형 영역에 대해 같은 방식의 압축을 시도함
# 이때 재귀를 사용

# 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return

# 분할 정복: 큰 문제를 작은 문제로 쪼개서 푸는 것. + 재귀.
# 이 정사각형 배열을 압축할 수 있는가?


def solution(arr):
    # 초기값
    answer = [0, 0]
    # 행, 열, 정사각형 크기
    def compress(y, x, size):
        base = arr[y][x]

        for i in range(y, y+size):
            for j in range(x, x+size):
                if arr[i][j] != base:
                    half = size // 2
                    #왼쪽 위 압축
                    compress(y, x, half)
                    #오른쪽 위 압축
                    compress(y, x+half, half)
                    #왼쪽 아래 압축
                    compress(y+half, x, half)
                    #오른쪽 아래 압축
                    compress(y+half, x+half, half)

                    return
        #여기까지 왔으면 전부 같은 값
        answer[base] += 1

    # 처음에는 arr전체를 하나의 영역으로 보고 시작한다.
    compress(0, 0, len(arr))

    return answer

print(solution([
    [1, 1],
    [1, 1]
]))
# 기대값: [0, 1]


print(solution([
    [0, 0],
    [0, 0]
]))
# 기대값: [1, 0]


print(solution([
    [1, 0],
    [0, 1]
]))
# 기대값: [2, 2]


print(solution([
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]))
# 기대값: [4, 9]


print(solution([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1]
]))
# 기대값: [10, 15]
