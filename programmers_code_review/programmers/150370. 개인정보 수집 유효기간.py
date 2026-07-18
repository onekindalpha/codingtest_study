
# 오늘 날짜를 의미하는 문자열 today
# 약관의 유효기간을 담은 1차원 문자열 배열 terms
# 개인정보의 정보를 담은 1차원 문자열 배열 privacies
# 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

# today 만드는 함수

# 오늘 날짜를 의미하는 문자열 today
# 약관의 유효기간을 담은 1차원 문자열 배열 terms
# 개인정보의 정보를 담은 1차원 문자열 배열 privacies
# 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

# today 만드는 함수
# 날짜 문자열을 총 일수로 바꾸는 함수
def to_days(date):
    year, month, day = map(int, date.split("."))

    total_day = year * 12 * 28 + month * 28 + day

    return total_day

def solution(today, terms, privacies):
    answer = []

    # 오늘 날짜를 총 일수로 바꾼다.
    today_day = to_days(today)

    # 약관종류에 따른 유효기간을 더하려면 정수화해서 일수로 저장
    # 유효기간만 추리는 딕셔너리 만들기
    terms_dict = {}

    for term in terms:
        alphabet, term_months = term.split()

        # 이 문제는 한 달을 28일로 계산한다.
        # 예를 들어 A 6이면 6 * 28 = 168일
        terms_dict[alphabet] = int(term_months) * 28

    # enumerate(privacies)는 리스트를 돌면서 순서번호와 값을 같이 꺼내주는 함수임.
    for i, privacy in enumerate(privacies):
        date, alphabet = privacy.split()

        # 개인정보 수집일을 총 일수로 바꾼다.
        collected_day = to_days(date)

        # 개인정보 수집일 + 약관 유효기간
        expire_day = collected_day + terms_dict[alphabet]

        # 만료일이 오늘보다 같거나 이전이면 파기 대상
        if expire_day <= today_day:
            print("결과: 파기 대상")
            # 문제의 개인정보 번호는 1번부터 시작하므로 파이썬 인덱스 i에 1을 더한다.
            answer.append(i + 1)
        else:
            print("결과: 보관 가능")

    return answer


print(solution(
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
))
# 예상 출력: [1, 3]
