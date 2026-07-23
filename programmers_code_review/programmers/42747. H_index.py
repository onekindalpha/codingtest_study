# n편중, >>h번 이상 인용된 논문이 h편 이상<<이고, 나머지 논문이 h번 이하 인용시
# h최댓값이 과학자의 h-index임
# 이 과학자의 h_index를 return
# 정렬문제임.
def solution(citations):
    # 내림차순. sort()는 반환값이 없음.
    citations.sort(reverse=True)
    answer = 0
    # 배열을 하나씩 돌면서 h에는 순번을 넣고, citation에는 인용 횟수를 넣는다.
    # enumerate = 반복하면서 순번도 같이 꺼내는 함수
    for h, citation in enumerate(citations, start=1):
        if citation >= h:
            answer = h
    return answer

print(solution([3, 0, 6, 1, 5]))