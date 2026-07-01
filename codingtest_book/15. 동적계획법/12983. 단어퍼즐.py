# 주어진 단어 조각들을 이용해서 주어진 문장을 완성하는 퍼즐입니다.
# 주어진 각 단어 조각들은 각각 무한개씩 있다고 가정합니다.
# 주어진 문장을 완성하기 위해 사용해야 하는 단어조각 개수의 최솟값을 return
# 사용가능한 단어 조각들을 담고 있는 배열 strs
# strs는 100 이하고 중복 없음.
# 문자열 형태. 단어 조각의 길이는 1 이상 5 이하
# t의 길이가 길다.
# dp로 여기까지 왔을 때 최소 조각 수 탐색

def solution(strs, t):
    # 단어조각들
    pieces = set(strs)
    # 문자열의 길이
    target_length = len(t)
    INF = 999999999
    # dp[i]는 t의 앞에서 i글자까지 만들 때 필요한 최소 조각 수
    # 일단 엄청 큰 값으로 채워둔다.
    dp = [INF] * ( target_length + 1 )
    # 빈 문자열은 조각 0개로 만들 수 있으니까.
    dp[0] = 0

    # 완성해야 하는 문자열 t를 앞에서부터 본다.
    for end in range(1, target_length +1):
        # 최대 5글자까지 있을 수 있으니까.
        for piece_length in range(1, 6):
            # 마지막에 붙일 글자를 어디서부터 시작하는지.
            start = end-piece_length
            if start <0:
                continue
            # 꺼낸 퍼즐조각의 문자열
            piece = t[start:end]
            # 만약 해당 piece가 실제 조각 목록에 있으면 dp[end]를 갱신
            # dp[start]까지 만든 뒤, piece하나를 붙이면 dp[end] 후보가 된다.
            # 그 후보들 중 최소 조각 수만 dp[end]에 남긴다.
            if piece in pieces:
                dp[end] = min(dp[end], dp[start] +1)

    if dp[target_length] == INF:
        return -1

    return dp[target_length]


print(solution(["ba","na","n","a"], "banana"))
# 3

print(solution(["app","ap","p","l","e","ple","pp"], "apple"))
# 2

print(solution(["ba","an","nan","ban","n"], "banana"))
# -1