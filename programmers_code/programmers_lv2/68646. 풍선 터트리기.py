# 일렬로 나열된 n개의 풍선, 모든 풍선에는 서로 다른 숫자가 터트려져 있음
# 인접한 두 풍선을 고르고 두 풍선 중 하나를 터트림
# 터진 풍선으로 인해 사이에 빈공간 생기면, 빈공간 없도록 밀착시킴
# 번호가 더 작은 풍선 터트리는 행위는 최대 1번만. 그 이후에는 번호가 더 큰 풍선만을 터트릴 수 있음
# 어떤 풍선이 최후까지 살아남을지.

# 일렬로 나열된 풍선들의 번호가 담긴 배열 a
# 풍선들을 1개만 남을 때까지 터트렸을 때 최후까지 남기는 것이 가능한! 풍선들의 개수를 return

# 예시에서 얻은 힌트: 각 번호별로 최후까지 남길 수 있는지? 일단 인접한 것끼리 비교함.
# => 여기서 놓친 포인트:
# a[i]보다 작은 값이 왼쪽에도 있고 오른쪽에도 있으면,
# a[i]는 마지막까지 남을 수 없다.

# 직관적인 코드 버전
def solution(a):
    n = len(a)

    if n == 1 or n == 2:
        return n

    # 중복제거를 위해 집합을 사용.
    # 어떤 풍선은 왼쪽 기준으로도 가능, 오른쪽 기준으로도 가능.
    # set은 중복 자동 제거.
    possible = set()

    # 1. 왼쪽에서 오른쪽으로 훑기
    # 왼쪽에서 봤을 때 새 최솟값이면 생존 가능
    left_min = a[0]
    possible.add(0)

    for i in range(1, n):
        current = a[i]

        if current < left_min:
            left_min = current
            possible.add(i)

    # 2. 오른쪽에서 왼쪽으로 훑기
    # 오른쪽에서 봤을 때 새 최솟값이면 생존 가능
    right_min = a[n - 1]
    possible.add(n - 1)

    # 시작, 끝, 이동폭
    # 0까지 가려면 끝값을 -1로 둔다.
    # range는 끝값을 포함하지 않기 때문.
    for i in range(n - 2, -1, -1):
        current = a[i]

        if current < right_min:
            right_min = current
            possible.add(i)

    return len(possible)


print(solution([9, -1, -5]))
# 3

print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
# 6