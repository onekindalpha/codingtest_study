# sorted( , key)
# n번째 글자가 같으면, 문자열 전체를 사전순으로 정렬한다.

def solution(strings, n):
    def make_sort_key(word):
        # 1순위와 2순위
        return (word[n], word)
    answer = sorted(strings, key=make_sort_key)
    # 짧게 줄이면
    # def soltuion(strings, n)
    #   return sorted(strings, key=lambda word : (word[n], word))도 가능
    return answer


