# 알아볼 수 없는 번호를 0
# 로또번호 6개
# # 당첨번호 6개
# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정
from re import match

#로또 번호 담은 배열 lottos
#당첨 번호 담은 배열 win_nums
#당첨가능한 최고순위와 처저순위를 차례대로 배열에 담아서 return
#0은 알아볼 수 없는 숫자
#0을 제오한 다른 숫자들은 lottos에 2개 이상 담겨있지 않음
def rank(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count == 4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else:
        return 6
def solution(lottos, win_nums):
    #win_nums를 set으로 바꾼다.
    win_nums = set(win_nums)
    zero_count = 0
    match_count = 0

#    lottos 숫자를 하나씩 본다.
    for i in lottos:
        if i == 0:
            zero_count += 1
        if i in win_nums:
            match_count += 1

    #최고 맞은 개수 = match + zero #제로를 모두 당첨번호라고 가정함
    top_count = match_count + zero_count

    #최저 맞은 개수 = match
    low_count = match_count

    return [rank(top_count), rank(low_count)]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# [3, 5]

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# [1, 6]

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
# [1, 1]