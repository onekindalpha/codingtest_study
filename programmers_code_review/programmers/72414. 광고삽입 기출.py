# 공익광고를 넣을 구간을 찾는 문제다.
# 단, return은 구간 전체가 아니라 광고 시작 시간이다.
# 광고 구간은 [start, start + adv_time)이다.
# 각 start마다 광고 구간 안의 총 시청량을 계산하고,
# 그 값이 가장 큰 start를 return한다.
# 같은 값이 여러 개면 가장 빠른 start를 return한다.
# 누적합 / 차분 배열 / 슬라이딩 윈도우

# 시간을 초로 변환한다.
def time_to_sec(time):
    HH, MM, SS = map(int, time.split(":"))
    return HH * 3600 + MM * 60 + SS


# 초를 다시 HH:MM:SS 형태로 변환한다.
def sec_to_time(seconds):
    HH = seconds // 3600
    MM = (seconds % 3600) // 60
    SS = seconds % 60

    # 정수로 출력하되, 최소 2자리로, 빈자리는 0으로 채운다.
    return f"{HH:02d}:{MM:02d}:{SS:02d}"


def solution(play_time, adv_time, logs):
    # 1. play_time을 초로 바꾼다.
    play_sec = time_to_sec(play_time)

    # 2. adv_time을 초로 바꾼다.
    adv_sec = time_to_sec(adv_time)

    # 3. 시청자 수를 기록할 배열을 만든다.
    # 처음에는 viewer_count[t] = t초에 시청자 수가 얼마나 변하는지
    # 누적합 이후에는 viewer_count[t] = t초의 실제 시청자 수
    viewer_count = [0] * (play_sec + 1)

    # 4. logs를 하나씩 확인한다.
    # 각 log는 "시작시간-종료시간" 형태다.
    for log in logs:
        start_time, end_time = log.split("-")

        # 시작시간을 초로 바꾼다.
        start_sec = time_to_sec(start_time)

        # 종료시간을 초로 바꾼다.
        end_sec = time_to_sec(end_time)

        # start_sec부터 시청자 1명 증가
        viewer_count[start_sec] += 1

        # end_sec부터 시청자 1명 감소
        viewer_count[end_sec] -= 1

    # 5. 누적합으로 초별 실제 시청자 수를 만든다.
    # 이 이후부터 viewer_count[t]는 t초에 실제로 보고 있는 시청자 수다.
    for current_time in range(1, play_sec + 1):
        viewer_count[current_time] += viewer_count[current_time - 1]

    # 6. 광고를 0초에 넣는다고 가정한다.
    # 0초부터 adv_sec 전까지의 시청자 수를 전부 더한다.
    # 이 값은 광고 구간의 총 시청량이다.
    current_ad_total_view_seconds = sum(viewer_count[0:adv_sec])

    # 현재까지 가장 큰 광고 총 시청량
    best_ad_total_view_seconds = current_ad_total_view_seconds

    # 현재까지 가장 좋은 광고 시작 시간
    best_start_time = 0

    # 7. 광고 시작 시간을 1초부터 하나씩 옮긴다.
    # 광고 구간을 오른쪽으로 1초 옮기면,
    # 이전 광고 구간의 맨 앞 초 시청자 수는 빠지고,
    # 새 광고 구간의 맨 뒤 초 시청자 수는 들어온다.
    for start_time in range(1, play_sec - adv_sec + 1):
        current_ad_total_view_seconds = (
            current_ad_total_view_seconds
            - viewer_count[start_time - 1]
            + viewer_count[start_time + adv_sec - 1]
        )

        # 지금 광고 구간이 지금까지 본 것보다 더 좋으면 갱신한다.
        # 같은 값이면 갱신하지 않는다.
        # 앞에서부터 탐색하므로 기존 best_start_time이 더 빠른 시작 시간이기 때문이다.
        if current_ad_total_view_seconds > best_ad_total_view_seconds:
            best_ad_total_view_seconds = current_ad_total_view_seconds
            best_start_time = start_time

    # 8. best_start_time을 다시 "HH:MM:SS" 형식으로 바꿔서 return한다.
    return sec_to_time(best_start_time)


print(solution(
    "02:03:55",
    "00:14:15",
    [
        "01:20:15-01:45:14",
        "00:40:31-01:00:00",
        "00:25:50-00:48:29",
        "01:30:59-01:53:29",
        "01:37:44-02:02:30"
    ]
))
# 기대값: "01:30:59"


print(solution(
    "99:59:59",
    "25:00:00",
    [
        "69:59:59-89:59:59",
        "01:00:00-21:00:00",
        "79:59:59-99:59:59",
        "11:00:00-31:00:00"
    ]
))
# 기대값: "01:00:00"


print(solution(
    "50:00:00",
    "50:00:00",
    [
        "15:36:51-38:21:49",
        "10:14:18-15:36:51",
        "38:21:49-42:51:45"
    ]
))
# 기대값: "00:00:00"


print(solution(
    "00:00:10",
    "00:00:03",
    [
        "00:00:00-00:00:03",
        "00:00:00-00:00:03"
    ]
))
# 기대값: "00:00:00"


print(solution(
    "00:00:10",
    "00:00:03",
    [
        "00:00:05-00:00:08",
        "00:00:05-00:00:08",
        "00:00:05-00:00:08"
    ]
))
# 기대값: "00:00:05"


print(solution(
    "00:00:06",
    "00:00:03",
    [
        "00:00:00-00:00:03",
        "00:00:03-00:00:06"
    ]
))
# 기대값: "00:00:00"