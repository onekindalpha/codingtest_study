# 1부터 n까지 서로 다른 정수 5개 오름차순 = 비밀코드. 맞춰야.
# m번 시도 가능.
# 입력한 정수 배열 q.
# 시스템응답(일치하는 개수)=비밀코드에 포함된 정수 개수 알려줌 = ans
# m번 시도 후, 비밀코드로 가능한, 정수 조합의 개수를 알고 싶음.
# 비밀코드로 가능한 정수 조합 개수 return

from itertools import combinations

def solution(n, q, ans):
    answer = 0

    for candidate in combinations(range(1, n + 1), 5):
        passed = True

        for i in range(len(q)):
            question = q[i]
            expected_count = ans[i]

            match_count = 0

            for number in question:
                if number in candidate:
                    match_count += 1

            if match_count != expected_count:
                passed = False
                break

        if passed:
            answer += 1

    return answer
print(solution(
    10,
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [3, 7, 8, 9, 10],
        [2, 5, 7, 9, 10],
        [3, 4, 5, 6, 7]
    ],
    [2, 3, 4, 3, 3]
))
# 예상 결과: 3