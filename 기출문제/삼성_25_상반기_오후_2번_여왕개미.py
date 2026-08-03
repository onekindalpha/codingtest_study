import sys
from io import StringIO

sys.stdin = StringIO("""7
100 5 2 4 7 8 15
400 1
400 2
200 50
400 2
300 5
400 3
""")
import heapq
import queue

# # bfs함수는 별도로 만들어야 겠음.
Q = int(input())
    # 둘째줄부터 Q줄 동안
houses = []
removed = []
#T초가 주어졌을 때 r마리로 모든 개미집을 정찰할 수 있는가?
def can_scout(T, r):
    #사용한 개미수
    ant_count = 0
    #현재 개미의 출발 위치 없음
    start_position = None
    #집 번호를 1번부터 마지막 번호까지 확인:
    for index in range(len(houses)):
        # 철거된 집은 검사하지 않음
        if removed[index]:
            continue
        current_position = houses[index]
        #print("현재 집 위치는", current_position)
        #아직 개미를 배치하지 않았으면
        if start_position is None:
            # 사용한 개미 수 += 1
            ant_count += 1
            #print("사용한 개미수", ant_count)
            # 현재 개미의 출발 위치 = 현재 집 좌표
            start_position = current_position
            #print("현재 개미 출발 위치", start_position)
        #현재 집 좌표 - 현재 개미 출발 좌표 > T라면: 그러니까 T보다 오래걸리면
        elif current_position - start_position > T:
            #새 개미를 현재 집에 배치
            ant_count += 1
            #print("사용한 개미수", ant_count)
            # 현재 개미의 출발 위치 = 현재 집 좌표
            start_position = current_position
            #print("현재 개미 출발 위치", start_position)
        # 사용한 개미 수가 r보다 많아지면
        if ant_count > r:
            #false반
            return False
    #true반환
    return True
#가능한 최소시간 탐색
def find_min_time(r):
    left = 0
    #오른쪽은 최대시간임.
    right = 1_000_000_000

    while left <= right:
        T = (left + right) // 2
        #print(T)
        #mid초 안에 r마리로 정찰 가능하면
        if can_scout(T, r):
            right = T -1
            #print(right)
        #불가능하면
        else:
            # T초로 불가능하므로 늘림
            left = T +1
            #print(left)
    return left
for i in range(Q):
    query = list(map(int, input().split()))
    #print(query)
    command = query[0]
    if command == 100:
        # 개미집 번호의 길이 1-index
        N = query[1]
        #개미집의 좌표
        houses=query[2:]
        removed = [False] * N
        #print("개미집들의 배열", houses)
        #print(len(houses))
        #여왕개미의 집
        #모든 집의 철거여부를 저장할 배열
        #print("철거여부 배열", removed)
    #개매집 건설
    elif command == 200:
        position = query[1]
        #print("추가할 개미집 위치", position)
        #개미집 건설 위치 x=p
        houses.append(position)
        #print("추가된 개미집 리스트", houses)
        removed.append(False)
        #print("추가된 철거여부", removed)
        # p는 xn보다 큼.
        # 개미집의 번호도 표시를 해야 하나봄.
        # 실제 값을 알려면
        #ant_houses[house_number - 1]
        # k번 째로 주어지는 개미집 번호는 N + K로 표현됨.
        # 파이썬 인덱스는 0부터 시작하니까.
    #개미집 철거
    elif command == 300:
        house_number = query[1]
        #print("철거할 개미집 번호", house_number)
        #철거 개미집 번호
        # 파이썬 인덱스는 0부터 시작하니까, 집번호는 하나 줄인거.
        removed[house_number -1] = True
        #print("철거한 개미집 번호를 바꿈", removed)

    #개미집 정찰
    elif command == 400:
        # 정찰 일개미 수 - 사실 r을 어디에 상요해야 하는지 잘 모르겠음.
        r = query[1]
        #print("정찰 일개미 수", r)
        answer = find_min_time(r)
        print(answer)



