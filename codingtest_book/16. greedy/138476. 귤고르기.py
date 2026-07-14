# k개 수확.
# 크기별로 분류했을때 서로 다른 종류의 수를 최소화
# 한상자에 담으려는 귤의 개수 k개, 귤의 크기를 담은 배열 tangerine
# 크기가 서로 다른 종류의 수의 최솟값
# 그리디는 지금 가장 좋아보이는 선택을 계속 하는 방법으로. 개수가 가장 많은 크기의 귤부터 고르기.
# 매순간 가장 좋아보이는 선택을 해도 전체 정답이 되는가?

from collections import Counter
# 크기별 개수를 센다. Counter는 개수를 세어주는 도구이다.

def solution(k, tangerine):
    counter = Counter(tangerine)
    # 귤 크기별 개수만 꺼내서, 큰 개수부터 정렬한다.
    counts = sorted(counter.values(), reverse=True)
    # 지금까지 고른 귤 개수
    picked_count = 0
    # 지금까지 사용한 귤 크기 종류 수
    kind_count = 0
    # 많은 개수부터 하나씩 더한다.
    for count in counts:
        # 뽑은 개수를 더한다.
        picked_count += count
        # 크기 종류를 하나씩 더한다.
        kind_count +=1

# 뽑은 개수가 k개 이상이 되면 멈춘다.
        if picked_count >= k:
            return kind_count
# 테스트 1
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))

# 예상 결과: 3


# 테스트 2
k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))
# 예상 결과: 2


# 테스트 3
k = 2
tangerine = [1, 1, 1, 1, 2, 2, 3]
print(solution(k, tangerine))
# 예상 결과: 1