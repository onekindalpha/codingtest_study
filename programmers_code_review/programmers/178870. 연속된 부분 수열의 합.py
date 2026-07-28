# 투포인터 문제란 인덱스 2개를 움직이면서 범위를 찾는 풀임.
# k = 목표 합
# total = 현재 보고 있는 구간의 합
# 비내림차순이라는 말이 힌트라서,
# 오른쪽으로 갈수록 값이 작아지지 않는다는 것을 알 수 있음.

def solution(sequence, k):
    #시작인덱스
    start = 0
    #현재 보고 있는 구간의 합
    total = 0
    # 가장 짧은 길이의 수열. 그리고 시작인덱스가 작은 것을 정답으로 제시해야 함.
    best_length = len(sequence)
    # start, end값을 미리 초기화함.
    answer = [0, len(sequence) - 1]
    # 합이 작으면 end가 오른쪽으로 이동
    # 합이 크면 start가 오른쪽으로 이동
    #end는 for문에 의해 매 반복 오른쪽으로 이동한다.
    #total이 k보다 작으면 별도 처리를 하지 않고 다음 반복에서 오른쪽 값을 더한다.
    #total이 k보다 크면 while문에서 왼쪽 값을 빼고 start를 오른쪽으로 이동한다.
    # end가 오른쪽으로 이동하면서 현재 구간에 sequence[end]를 추가한다.
    for end in range(len(sequence)):
        total += sequence[end]
        ## 현재 구간 합이 목표 합 k보다 크면
        # 왼쪽 값을 빼면서 start를 오른쪽으로 이동한다.
        while total > k:
                total -= sequence[start]
                start +=1
        # 현재 구간 합이 k이면 [start, end]가 정답 후보가 된다.
        if total == k:
            current_length = end - start + 1
            # 더 짧은 구간이면 정답을 갱신한다.
            # 길이가 같으면 갱신하지 않는다.
            # 그래야 앞쪽에 나온 구간이 유지된다.
            if current_length < best_length:
                best_length = current_length
                answer = [start, end]
    return answer

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))