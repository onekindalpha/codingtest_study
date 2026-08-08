from collections import deque

def solution(cards):
    n = len(cards)

    visited = [False] * n
    box_groups = {}
    turn = 0

    # 모든 상자를 시작점 후보로 본다
    for start in range(n):
        # 이미 열린 상자면 새 그룹 시작 안 함
        if visited[start]:
            continue

        queue = deque()
        box_group = []

        queue.append(start)

        while queue:
            position = queue.popleft()

            # 이미 열린 상자를 만나면 현재 그룹 종료
            if visited[position]:
                break

            # 현재 상자를 연다
            visited[position] = True

            # 그룹에 현재 상자 추가
            # position은 0-based라서 상자 번호로 보고 싶으면 +1
            box_group.append(position + 1)

            # 다음에 열 상자 번호
            next_card_idx = cards[position] - 1

            queue.append(next_card_idx)

        box_groups[turn] = box_group
        turn += 1

    print(box_groups)

    # 그룹 크기만 뽑음
    group_sizes = []

    for i in range(len(box_groups)):
        group_sizes.append(len(box_groups[i]))

    # 그룹이 1개뿐이면 두 번째 그룹이 없으므로 점수 0
    if len(group_sizes) < 2:
        return 0

    # 가장 큰 그룹 2개를 골라야 최고 점수
    group_sizes.sort(reverse=True)

    return group_sizes[0] * group_sizes[1]


print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
# 카드번호에 해당하는 번호를 가진 상자를 계속 열음
# 열어야 하는 상자가 이미 열려있을 땎자ㅣ 반복.
# 이렇게 연 것은 1번 상자.
# 다른 상자들과 섞이지 않도록 따로 둠.
# 만약, 1번 상자 그룹을 제외하고 남는 상자가 없음녀 그대로 게임 종료, 점수 0점
# 그렇지 않다면, 남은 상자 중 다시 임의 상자 하나 골라 같은 방식으로 이미 열려있는 상자 만날때까지 상자 염.
# 이렇게 열면 2번 상자 그룹
# 1번 그룹 상자 수와 2번 상자 그룹에 속한 상자 수 곱한 값이 게임의 점수
# 상자안 카드번호가 순서대로 담긴 배열, 이 게임에서 얻을 수 있는 최고 점수 리턴.

#
#
# def solution(cards):
#     answer = 0
#     return answer