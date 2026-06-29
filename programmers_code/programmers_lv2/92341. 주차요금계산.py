# 입차 , 출차 시간으로 총 주차 시간 누적
# 출차 기록 없으면 23:59에 출차 처리
# 차량 번호 오름차순으로 주차 요금 계산

def time_to_minute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def calculate_fee(total_time, fees):
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    if total_time <= base_time:
        return base_fee
    extra_time = total_time - base_time
    units = (extra_time + unit_time -1) // unit_time
    return base_fee + units * unit_fee


def solution(fees, records):
    in_time = {}
    total_time = {}

    for record in records:
        time, car_number, status = record.split()
        minute = time_to_minute(time)

        if status == "IN":
            in_time[car_number] = minute
            if car_number not in total_time:
                total_time[car_number] = 0
        else:
            parking_time = minute - in_time[car_number]
            total_time[car_number] += parking_time
            del in_time[car_number]
    end_time = time_to_minute("23:59")
    for car_number in in_time:
        parking_time = end_time - in_time[car_number]
        total_time[car_number] += parking_time

    answer = []

    for car_number in sorted(total_time.keys()):
        fee = calculate_fee(total_time[car_number], fees)
        answer.append(fee)
    return answer
print(solution(
    [180, 5000, 10, 600],
    [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT"
    ]
))
# 기대값: [14600, 34400, 5000]


print(solution(
    [120, 0, 60, 591],
    [
        "16:00 3961 IN",
        "16:00 0202 IN",
        "18:00 3961 OUT",
        "18:00 0202 OUT",
        "23:58 3961 IN"
    ]
))
# 기대값: [0, 591]


print(solution(
    [1, 461, 1, 10],
    [
        "00:00 1234 IN"
    ]
))
# 기대값: [14841]