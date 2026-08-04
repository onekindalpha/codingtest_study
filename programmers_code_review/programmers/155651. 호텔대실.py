import heapq
def to_minutes(time):
    hour, minute = map(int, time.split(":"))
    #print(hour, minute)
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    book_time_minutes = []
    for start, end in book_time:
        book_time_minutes.append([to_minutes(start), to_minutes(end)])
    book_time_minutes.sort(key=lambda x: x[0])
    rooms= []

    for start, end in book_time_minutes:
        #rooms가 비어있지 않고,
        #가장 빨리 비는 방의 사용 가능 시간 <= 현재 예약 시작 시간
        # 이면 그 방을 재사용할 수 있음
        if rooms and rooms[0] <= start:
            # 가장 빨리 비는 방을 꺼냄
            # 이 방에 현재 예약을 다시 넣을 예정임
            heapq.heappop(rooms)
            print(rooms)
        #현재 예약이 끝난 뒤 청소 10분 까지 포함해서
        # 이방이 다시 사용가능한 시간을 rooms에 넣음
        heapq.heappush(rooms, end +10)
        print(rooms)
    #방을 재사용할 수 없으면 pop을 안 하고 push만 해서 rooms는 필요한 방의 개수가 됨
    # rooms에 남아있는 개수 = 동시에 필요했던 객실 수
    #print(len(rooms))
    answer = len(rooms)
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]	))