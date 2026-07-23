from collections import deque

# 프로세스의 중요도가 순서대로 담긴 배열 priorities
# 몇번째로 실행되는지 알고싶은 프로세스의 위치 location
def solution(priorities, location):
    # 실행 대기 큐를 만든다.
    # deque는 맨 앞에서 꺼내는 popleft()와 맨 뒤에 넣는 append()를 사용할 수 있다.
    queue = deque()

    # priorities의 각 프로세스를 큐에 넣는다.
    # i = 프로세스의 원래 인덱스
    # priorities[i] = 프로세스의 우선순위
    for i in range(len(priorities)):
        # (원래 인덱스, 우선순위) 형태로 큐에 넣는다.
        # 원래 인덱스가 필요한 이유: location 위치의 프로세스를 찾기 위해서.
        queue.append((i, priorities[i]))

    # 실행된 프로세스 개수
    answer = 0

    # 큐가 남아있을때까지는 계속 반복함.
    while queue:
        # 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
        idx, priority = queue.popleft()
        # idx = 원래 인덱스
        # priority = 우선순위

        # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        # priority보다 큰 값이 queue안에 있는지 확인
        # 숫자가 클 수록 우선순위가 높음.
        if any(priority < other_priority for other_idx, other_priority in queue):
            # 더 큰 우선순위가 있으면 현재 프로세스는 실행하지 않고 큐 맨 뒤로 보낸다.
            queue.append((idx, priority))
        # 3. 만약 그런 프로세스가 없다면(더 큰 우선순위가 없다면) 방금 꺼낸 프로세스를 실행합니다.
        else:
            answer += 1
            # 3. 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료된다.
            # 방금 실행한 프로세스가 location 위치의 프로세스라면 실행 순서를 반환한다.
            if idx == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))