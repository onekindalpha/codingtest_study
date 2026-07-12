# 거스름돈 문제는 그리디 알고리즘으로 풀 수 없다고 했지만, 만일
# 거스름돈 화폐 간의 관계가 서로 배수 관계라면 그리디 알고리즘으로 풀 수 있음
# 이 말은 큰 단위가 작은 단위 여러 개로 정확히 바뀔 수 있기 때문에, 큰 돈을 먼저 쓰는게 손해가 아님
#거스름돈
amount = 0
#화폐단위
#변환하는값의 화폐단위는 내림차순

#코드작성
def solution(amount):
    coins = [1, 10, 50, 100]
    coins.sort(reverse=True)

    answer = []
    for coin in coins:
        # 현재 화폐 단위로 최대한 거슬러 줄 수 있는 동전의 갯수를 구한다. 
        count = amount // coin
        answer.extend([coin]*count)
        #정산이 완료된 거스름돈을 제외함
        amount %= coin
    return answer

print(solution(123))

print(solution(350))



