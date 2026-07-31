def time_to_minutes(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


def solution(plans):
    plans.sort(key=lambda x: x[1])

    sorted_plans = []

    for name, start, playtime in plans:
        start_minutes = time_to_minutes(start)
        sorted_plans.append((name, start_minutes, int(playtime)))

    answer = []
    stack = []

    for i in range(len(sorted_plans) - 1):
        current_name, current_start_minutes, current_playtime = sorted_plans[i]
        next_start_minutes = sorted_plans[i + 1][1]

        # 현재 과제 시작 시각부터 다음 과제 시작 시각까지 쓸 수 있는 시간
        available_time = next_start_minutes - current_start_minutes

        if current_playtime <= available_time:
            # 현재 과제를 다음 과제 시작 전까지 끝낼 수 있음
            answer.append(current_name)

            # 현재 과제를 끝내고도 남은 빈 시간
            free_time = available_time - current_playtime

            # 빈 시간이 있고, 멈춘 과제가 있으면 최근에 멈춘 과제부터 이어서 진행
            while stack and free_time > 0:
                paused_name, remaining_playtime = stack.pop()

                if remaining_playtime <= free_time:
                    # 빈 시간 안에 멈춘 과제를 끝낼 수 있음
                    answer.append(paused_name)

                    # 멈춘 과제를 끝낸 만큼 빈 시간을 줄임
                    free_time -= remaining_playtime

                else:
                    # 빈 시간 안에 멈춘 과제를 끝낼 수 없음
                    # free_time만큼 진행하고, 남은 작업 시간을 다시 stack에 넣음
                    stack.append((paused_name, remaining_playtime - free_time))

                    # 빈 시간을 전부 썼으므로 0
                    free_time = 0

        else:
            # 현재 과제를 다음 과제 시작 전까지 끝낼 수 없음
            # 나중에 이어서 해야 할 남은 작업 시간
            remaining_playtime = current_playtime - available_time

            # 멈춘 과제를 stack에 저장
            stack.append((current_name, remaining_playtime))

    # 마지막 과제는 뒤에 새 과제가 없으므로 완료됨
    answer.append(sorted_plans[-1][0])

    # 모든 새 과제가 끝난 뒤, 멈춘 과제를 최근 순서대로 완료
    while stack:
        paused_name, remaining_playtime = stack.pop()
        answer.append(paused_name)

    return answer