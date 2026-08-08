# n번째 문자열에서 앞에서부터 pos칸까지 1이 몇개인지.
def count_one(n, pos):
    #1번째 부터 pos번째까지의 1의 개수
    # pos는 몇 칸 볼 것인지를 의미함
    # 아무것도 보지 않기 때문에 0을 리턴함.
    if pos <= 0:
        return 0
    # n은 1부터만 가능하다.
    if n == 0:
        return 1
    # n-1을 치환한 결과이니까.
    block_size = 5 ** (n-1)
    one_count = 4 ** (n-1)
    base = "11011"
    #pos칸까지 봤을때, s1의 앞글자 몇개를 완전히 지나갔는지
    passed = pos // block_size
    #다음 글자 안에서 몇 칸을 더 봐야하는지
    remain = pos % block_size
    answer = 0
    # 완전히 지나간 S1의 글자들을 확인
    for i in range(passed):
        if base[i] == "1":
            answer += one_count
        # base[i] == "0"이면 1이 없으니까 아무것도 안 더함
    #아직 남은 칸이 있다면,
    # 다음 글자가 1인지 0인지 확인
    if remain > 0:
        if base[passed] == "1":
            answer += count_one(n -1, remain)
        # base[passed] =="0"이면 전부 0이라서 더할 게 없음
    return answer

def solution(n, l, r):

    return count_one(n, r) - count_one(n, l-1)

print(solution(2, 4, 17))