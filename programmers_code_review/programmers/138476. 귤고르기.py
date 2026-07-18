# 크기가 서로 다른 종류의 수의 최솟값
# 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine

# 크기가 서로 다른 종류의 수의 최솟값 return

# 해시맵 같음. 크기 몇개인거 몇개.
# 서로 다른 종류의 수의 최솟값을 올릴려면
# 개수가 큰것들을 먼저 담으려면 어떻게 정렬해야 하지?
# 그리디 같음

from collections import Counter
def solution(k, tangerine):
    cnt = Counter(tangerine)
    # print(cnt)
    # print(cnt.most_common())
    # 귤 종류 수 최솟값만 구할 때는 귤 크기 번호는 필요 없음.
    # 개수만 큰 순서로 쓰면 됨.
    counts = sorted(cnt.values(), reverse=True)
    #print(counts)
    total = 0
    answer = 0

    for c in counts:
        total += c
        answer +=1

        if total >= k:
            return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
# 3

print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
# 2

print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
# 1

print(solution(5, [1, 1, 1, 2, 2, 3, 3, 4]))
# 3