# 민호가 센터임. 근데 enroll에 민호의 이름은 없음.
# 영업이익의 10%에 해당하는 것을 추천인에게 배분함. 자신은 이를 뺀 나머지를 가짐.
# 영역이익의 10%를 배분받은 타인은 또 그의 10%퍼센트를 자신을 추천해준 사람에게 배분. 결국 꼭대기는 center민호임
# 10%는 원 단위에서 절사. 10%가 1원 미만인 경우 이득을 분배하지 않고 가짐.
# 판매원의 이름을 담은 배열 enroll. 조직에 참여한 순서임.
# 판매원을 참여시킨 다른 판매원의 이름을 담은 배열 referral
# 판매량 집계 데이터의 판매원 이름을 나열한 배열 seller
# 판매량 집계 데이터의 판매 수량을 나열한 배열 amount
# 각 판매원이 득한 이익금을 나열한 배열을 return
# 추천인이 없을 경우 "-"
# 칫솔한개의 이익 100원

def solution(enroll, referral, seller, amount):
    # 풀이를 쉽게 하기 위해 가상의 표를 만듦. 내 바로 위 추천인이 뭔지
    # 사람이름을 넣으면 추천인을 알려주는 딕셔너리
    referrer = {}
    income = {}

    # 사람별 추천인 이름을 저장한다. 수익은 0원으로 초기화.
    for i in range(len(enroll)):
        member = enroll[i]
        ref = referral[i]

        referrer[member] = ref
        income[member] = 0

    # 판매기록 하나씩 처리
    for i in range(len(seller)):
        current = seller[i] # 현재 돈을 받을 사람
        money = amount[i] * 100 #판매 수익

        while current != "-" and money > 0:
            give_to_referrer = money // 10
            keep = money - give_to_referrer

            income[current] += keep

            current = referrer[current]
            money = give_to_referrer

    # enroll 순서대로 수익을 꺼내서 정답 만들기
    answer = []
    for member in enroll:
        answer.append(income[member])

    return answer


# 테스트 1
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
# 예상 결과: [360, 958, 108, 0, 450, 18, 180, 1080]


# 테스트 2
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]

print(solution(enroll, referral, seller, amount))
# 예상 결과: [0, 110, 378, 180, 270, 450, 0, 0]

