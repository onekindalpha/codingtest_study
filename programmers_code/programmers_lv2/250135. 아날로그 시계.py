# pccp 문제
# 알림이 울리는 횟수를 세기 시작한 시각은 0시 5분 30초임
# 초침과 시침이 겹칠 때 알람이 한번 울림, 초, 시, 분이 겹칠때도.
# 알람이 울린 횟수를 세는 문제.
# h1, m1, s1, h2, m2, s2
# 알람이 울리는 횟수를 return
# 두 바늘의 각도가 같을 때. 두 바늘이 같은 곳을 가리킨다는 것.
# 시침 12시간 마다 한번. 분침 60분마다 한번. 초침 60초에 한번.
# 시계 위치를 숫자로 바꿔야 함.
# 12시 방향 0도, 3시 방향 90도, 6시 방향 180도, 9시 방향 270도, 다시 12시 방향 360도 또는 0도
# h1_count, m1_count, s1_count
# h = 60초에 한 바퀴 (60초)
# m = 3600초에 한 바퀴 (60분 곱하기 60초)
# s = 43200에 한 바퀴 (12시간 곱하기 3600초)
# h2_count, m2_count, s2_count

# 2단계: 특정 시각에서 초점, 분침, 시침의 위치 구하기.
def get_angles(time):
    # (참고) 한 바퀴는 360도.
    # 초침은 1초에 6도 움직임 (360도 / 60초 = 6)
    # 바퀴를 빼고 현재 위치를 알기 위해서 % 360을 함.
    second_angle = (time * 6) % 360
    # 분침은 1초에 0.1도 움직임 (360도 / 3600초 = 0.1)
    minute_angle = (time * 0.1) % 360
    # 시침은 1초에 1/120도 움직임 (360도 / 43200초 = 1/120)
    hour_angle = (time * (1/120)) % 360
    return second_angle, minute_angle, hour_angle

# 4단계. 이미 시작 시간부터 이미 겹쳐있었던 경우
def is_alarm_at(time):
    second_angle, minute_angle, hour_angle = get_angles(time)

    return second_angle == minute_angle or second_angle == hour_angle

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # 1단계: 시작 시간과 끝 시간을 초 단위로 바꾸기.
    # 알람을 세기 시작하는 시각을 초로 바꾼 값
    start_time = h1 * 3600 + m1 * 60 + s1
    # 알람을 세는 것을 끝내는 시각을 초로 바꾼 값
    end_time = h2 * 3600 + m2 * 60 + s2
    # 시작 시각에 이미 초침이 분침 또는 시침과 겹쳥 있으면 알람을 1번 세고 시작한다.
    if is_alarm_at(start_time):
        answer += 1  # pccp 문제
    # 3단계: 시작 시각에서 끝 시각까지 1초씩 보면서, 그 1초 사이에 알람이 울렸는지 확인한다.
    for time in range(start_time, end_time):
        # 초침이 시침이나 분침과 겹쳐야 함.
    # 초침 + 시침 겹치기. meet_hour
    # 초침과 분침 겹치기. meet_minute
    # 셋 다 겹쳐도 알람은 1번
        # 현재 시간을 넣고, 시침, 분침, 초침의 위치를 찍는다. 초 단위로.
        # 다음 시간을 넣고, 시침, 분침, 초침의 위치를 찍는다. 초 단위로.
        current_second, current_minute, current_hour = get_angles(time)
        next_second, next_minute, next_hour = get_angles(time+1)
        # 근데 초침은 60초마다 0으로 바뀌기 때문에. 360도 위치라고 보정할 필요가 있다.
        if next_second == 0:
            next_second = 360
        if next_minute == 0:
            next_minute = 360
        if next_hour == 0:
            next_hour = 360
        # 현재 초침이 현재 분침보다 뒤에 있고, 1초 뒤 초침이 1초 뒤 분침보다 앞에 있는가?
        # 그리고 초침이 현재 시침보다 뒤에 있고, 1초 뒤 초침이 1초 뒤 시침보다 앞에 있는가?
        # 이 유는 초침이 제일 빠르기 때문이다.
        # 그니까 알람이 울렸는가다.
        meet_minute = current_second < current_minute and next_second >= next_minute
        meet_hour = current_second < current_hour and next_second >= next_hour
        # 알람이 울렸으면 답안에 1개를 더한다.
        # 다만, 시분초가 동시에 만나는 12시 정각이라고 하면 -1을 한다.
        if meet_minute and meet_hour and time +1 == 43200:
            answer -= 1
        if meet_minute:
            answer += 1
        if meet_hour:
            answer += 1

    return answer
# 테스트 코드
print(solution(0, 5, 30, 0, 7, 0))        # 2
print(solution(12, 0, 0, 12, 0, 30))      # 1
print(solution(0, 6, 1, 0, 6, 6))         # 0
print(solution(11, 59, 30, 12, 0, 0))     # 1
print(solution(11, 58, 59, 11, 59, 0))    # 1
print(solution(1, 5, 5, 1, 5, 6))         # 2
print(solution(0, 0, 0, 23, 59, 59))      # 2852