# (r, c) n개의 포인트.
# 로봇 x대. 상하좌우로 이동. 1만큼씩. 1초마다.
# 최단 경로 탐색. r가 변하는 이동을 c좌표가 변하는 이동보다 먼저함.
# 같은 좌표에 2대 이상 로봇이 모인다면 충돌 가능 위험 상황임.
# 궁금한건 현재 상황대로 로봇이 움직일 때 위험한 상황이 총 몇 번 일어나는지.
# ex.어떤 시간에 여러 좌표에서 위험 상황이 발생시 그 횟수를 모두 더함.
# 운송 포인트 n개를 모두 담은 2차원 정수 배열 points
# 로봇 x대의 경로를 담은 2차원 정수 배열 routes은 로봇이 바문할 포인트 번호 목록
# 모든 로봇이 운송을 마칠 때까지 발생하는 위험한 상황의 횟수를 return

#1. 로봇 한대의 시간별 위치 리스트를 만든다.
#2. 모든 로봇에 대해 시간별 위치 리스트를 만든다.
#3. 같은 시간에 같은 좌표가 몇 번 나오는지 센다.
#4. 2대 이상 모인 좌표가 있으면 위험 상황 +1

def solution(points, routes):
    # 모든 로봇의 시간표를 담는 통. 로봇별 시간표를 따로 따로 담음.
    all_paths = []
    # 라우트를 받아서 로봇 한대의 시간표를 만들기.
    def make_path(route):
        path = []
            #route하나를 받아서 그 로봇이 시간별로 어디 있느지 리스트로 만든다.
        start_point = route[0]
        # 포인트 번호를 실제 좌표로 바꾼다.
        r, c = points[start_point -1]
        # 모든 로봇의 시간표를 담는 통에 넣는다.
        path.append((r, c))
        # 로봇을 다음 포인트까지 한 칸씩 움직인다.
        for point_num in route[1:]:
            target_r, target_c = points[point_num -1]
            # r좌표 먼저 이동
            while r != target_r:
                if r < target_r:
                    r += 1
                else:
                    r -= 1

                path.append((r, c))
            # c좌표 이동
            while c != target_c:
                if c < target_c:
                    c+= 1
                else:
                    c-=1
                path.append((r, c))
                # 로봇 한대의 시간표
        return path
    # 모든 로봇의 시간표를 하나씩 만들어서 all_paths에 넣음.
    for route in routes:
        path = make_path(route)
        all_paths.append(path)

    # 같은 시간에 같은 좌표에 로봇이 몇 대 있는지 셈.
    # 시간별로 검사.
    answer = 0
    max_time = max(len(path) for path in all_paths)
    for t in range(max_time):
        # 현재 t초에 , 각 좌표마다 로봇이 몇 대 있는지 적는 표.
        count_by_position = {}
        # 각 로봇의 t초 위치 확인
        for path in all_paths:
            # 로봇이 아직 운송중일때만 셈
            if t < len(path):
                position = path[t]
                if position not in count_by_position:
                    count_by_position[position] = 0
                count_by_position[position] += 1
        #같은 시간에 같은 좌표에 2대 이상 있으면 위험 상황 +1
        for count in count_by_position.values():
            if count >= 2:
                answer +=1
    return answer

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
# 1
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
# 9
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))
# 0