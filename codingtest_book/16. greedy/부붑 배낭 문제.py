# 무게 당 가치가 가장 높은 짐부터 최대한 넣는 점이 그리디 알고리즘임

def solution(items, weight_limit):
    # 1. 무게당 가치가 높은 순서로 정렬
    # items를 정렬하는데, 무게당 가치 / 무게. 큰 값부터 정렬.
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    # 선택한 물건들의 총 가치.
    total_value = 0
    # 남은 무게 한도 저장
    remain = weight_limit
    # 2. 가치가 높은 점부터 하나씩 보기
    for weight, value in items:
    # 배낭이 꽉 찼으면 종료
        if remain ==0:
            break

    # 3-1. 짐을 통째로 넣을 수 있으면
        if remain>=weight:
            total_value+=value
            remain -= weight

    # 3-2. 짐을 통째로 못 넣으면 쪼개서 넣기
        else:
            # 남은 용량 만큼만 짤라넣는 코드.
            # 키로 당 가치로 환산한후 남은용량에 넣는다.
            # 그리고 총 가치에 더한다.
            total_value += (value / weight ) * remain
            remain = 0

    return total_value

print(solution([[10, 19], [7, 10], [6, 10]], 15))

print(solution([[10, 60], [20, 100], [30, 120]], 50))