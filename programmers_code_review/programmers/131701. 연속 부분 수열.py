# 원소가 합을 구한 값들임
# 원형배열 + 완전탐색+슬라이싱+sum+set에서, 효율성을 위해 누적합 변수+set중복제거
# 자료구조는 set
def solution(elements):
    # 중복되는 값들 제외한 후
    answer_set = set()
    n = len(elements)
    extended = elements * 2
    #각 길이마다 시작위치 0부터 4까지 반복
    for start in range(n):
        # 연속 부분 수열 묶음의 합
        # 개선 부분: 누적합 변수 방식
        total = 0
        # 느린 부분(1) : 리스트를 새로 만들기 때문에
        #part = extended[start:start + length]
        # 느린 부분(2) : 새 리스트를 다시 순회하기 때문에.
        # 연속 부분 수열 묶음의 합
        #total = sum(part)
        # 길이 1부터 5까지 반복
        for length in range(1, n + 1):
            #start에서 시작해서 length개를 더한 값
            # 개선 부분: 누적합 변수 방식
            total += extended[start + length -1]
            # 서로 다른 합만 저장
            answer_set.add(total)
    return len(answer_set)