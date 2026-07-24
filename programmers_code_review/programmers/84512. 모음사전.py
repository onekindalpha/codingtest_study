# 길이 5이하
# A, AA, 마지막 UUUUU
# 완전탐색 + 재귀 DFS
# DFS를 쓰는 이유 = 사전 순서가 A를 끝까지 타고 내려가는 순서라서
def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    # word를 받으면 몇번째 단어인지 리턴해야 함
    words = []

    # 사전은 완전탐색으로 만든다.
    def dfs(current):
        # 빈 문자열은 사전에 안 넣음
        if current != "":
            words.append(current)
        # 길이 5가 되면 더 붙이지 않음
        if len(current)==5:
            return
        # 현재 단어 뒤에 모음 하나씩 붙이기
        for vowel in vowels:
            dfs(current + vowel)
    dfs("")
    # 몇 번째 단어인지 반환
    return words.index(word) + 1

