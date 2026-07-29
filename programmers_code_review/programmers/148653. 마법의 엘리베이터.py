# 층과 버튼을 더해서 0보다 작으면 움직이지 않음
# 0이 가장 아래층. 엘리베이터는 현재 민수층
# 버튼 한번당 마법의 돌 한개 사용.
# 마법의 돌 아끼기
# 어떤 층에서 0층까지 가기 위해 필요한 마버돌의 최솟값
# 마법의 엘리베이터에는 -1, +1, -10, +10, -100, +100 등과 같이 절댓값이 10c (c ≥ 0 인 정수) 형태인 정
# storey가 엄청 높을 수 있음.
#
# +1 4번, -10 2번. 이게 마법의 돌이 다인가. 아니지 -1도 있ㄱ네
# 사실상 버튼을 마법의 돌이라고 보는 듯함.
# 마법의 돌의 최소 개수. 마법의 돌 숫자는 임의인가...음....

def solution(storey):
    answer = 0
    renewed = storey
    digit = 1

    while renewed > 0:
        # 매 반복마다 갱신된 renewed 기준으로 문자열을 다시 만든다.
        storey_str = str(renewed)

        # digit = 1이면 일의 자리
        # digit = 2이면 십의 자리
        # digit = 3이면 백의 자리
        index = len(storey_str) - digit

        # 더 이상 볼 자리가 없으면 종료
        if index < 0:
            break

        char = storey_str[index]
        current_num = int(char)

        # 현재 자리값
        unit = 10 ** (digit - 1)

        if current_num < 5:
            # 현재 자리 숫자만큼 현재 자리값을 뺀다.
            minus_score = current_num * unit
            minus_count = minus_score // unit

            answer += minus_count
            renewed = renewed - minus_score

        elif current_num > 5:
            # 현재 자리 숫자를 다음 10단위로 올린다.
            plus_score = (10 ** digit) - (current_num * unit)
            plus_count = plus_score // unit

            answer += plus_count
            renewed = renewed + plus_score
        #5일때는, 왼쪽을 보고 판단해야 하는 이유가
        #일단 5는 올리나 내리나 비용이 같기 때문임.
        #45
        # 내림:
        # 45 → 40 : 5번
        # 40 → 0  : 4번
        # 총 9번
        #
        # 올림:
        # 45 → 50 : 5번
        # 50 → 0  : 5번
        # 총 10번
         #65
        #
        # 내림:
        # 65 → 60  : 5번
        # 60 → 100 : 4번
        # 100 → 0  : 1번
        # 총 10번
        #
        # 올림:
        # 65 → 70  : 5번
        # 70 → 100 : 3번
        # 100 → 0  : 1번
        # 총 9번
        else:
            next_index = index - 1
            if next_index >= 0:
                next_num = int(storey_str[next_index])
            else:
                next_num = 0
            if next_num >= 5:
                plus_score = (10 ** digit) - (current_num * unit)
                plus_count = plus_score // unit
                answer += plus_count
                renewed = renewed + plus_score
            else:
                minus_score = current_num * unit
                minus_count = minus_score // unit

                answer += minus_count
                renewed = renewed - minus_score
        # 다음 자리로 이동
        digit += 1

    return answer

print(solution(16))    # 6
print(solution(2554))  # 16
print(solution(3000))  # 3
print(solution(45))    # 9