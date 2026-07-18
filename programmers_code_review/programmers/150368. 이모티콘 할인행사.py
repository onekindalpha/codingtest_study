# 이모티콘 플러스 가입자 수 최대 vs 이모티콘 판매액 최대 중에 전자가 이김.
# 할인율 10, 20, 30, 40
# 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매
# 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 구매를 모두 취소하고 이뫁티콘 플러스에 가입함.
# 최대한 달성시, 가입자 수와 판매애 ㄱ반환

from itertools import product

def solution(users, emoticons):
    discount_options = [10, 20, 30, 40]
    best_plus_count = 0
    best_sales = 0
# 할인율 조합을 모두 해보기
    for discounts in product(discount_options, repeat=len(emoticons)):
        plus_count = 0
        sales = 0

        for user in users:
            user_discount = user[0]
            user_limit = user[1]

            buy_price = 0

            for i in range(len(emoticons)):
                discount = discounts[i]
                price = emoticons[i]
                # 이모티콘 할인율이 사용자 기준 할인율보다 높거나 같으면 산다.
                if discount >= user_discount:
                    sale_price =  price * (10 - discount) // 100
                    buy_price += sale_price

            if buy_price >= user_limit:
                plus_count += 1
            else:
                sales+= buy_price

        if plus_count > best_plus_count:
            best_plus_count = plus_count
            best_sales = sales
                # 가입자 수가 같으면 판매액이 더 큰 쪽으로 바꾼다.
        elif plus_count == best_plus_count and sales > best_sales:
            best_sales = sales
    return [best_plus_count, best_sales]

from itertools import product

def solution(users, emoticons):
    discount_options = [10, 20, 30, 40]

    best_plus_count = 0
    best_sales = 0

    for discounts in product(discount_options, repeat=len(emoticons)):
        plus_count = 0
        sales = 0

        for user in users:
            user_discount = user[0]
            user_limit = user[1]

            buy_price = 0

            for i in range(len(emoticons)):
                discount = discounts[i]
                price = emoticons[i]

                if discount >= user_discount:
                    sale_price = price * (100 - discount) // 100
                    buy_price += sale_price

            if buy_price >= user_limit:
                plus_count += 1
            else:
                sales += buy_price

        if plus_count > best_plus_count:
            best_plus_count = plus_count
            best_sales = sales

        elif plus_count == best_plus_count and sales > best_sales:
            best_sales = sales

    return [best_plus_count, best_sales]


# 테스트 코드
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# [1, 5400]

print(solution(
    [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
    [1300, 1500, 1600, 4900]
))
# [4, 13860]