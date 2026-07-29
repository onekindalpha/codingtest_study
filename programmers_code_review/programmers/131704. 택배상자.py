def solution(order):
    # 보조 컨베이어 벨트
    # 메인 컨베이어에서 당장 트럭에 못 싣는 상자를 넣는다.
    stack = []

    # 트럭에 실은 상자 개수
    answer = 0

    # 전체 상자 개수
    n = len(order)

    # 메인 컨베이어에서 다음에 나올 상자 번호
    # 문제에서 메인 컨베이어는 1번 상자부터 n번 상자까지 순서대로 나온다.
    box = 1

    # need = 지금 트럭에 실어야 하는 상자 번호
    for need in order:

        # 메인 컨베이어 앞 상자 box가 need보다 작으면
        # need가 나올 때까지 box들을 보조 컨베이어에 넣는다.
        #
        # 예: need = 4, box = 1
        # 1, 2, 3은 지금 트럭에 못 싣는다.
        # 그래서 stack에 넣는다.
        while box <= n and box < need:
            stack.append(box)

            # box번 상자를 메인 컨베이어에서 꺼냈으므로
            # 다음 상자로 이동한다.
            box += 1

        # 메인 컨베이어 앞 상자가 need면
        # 트럭에 바로 싣는다.
        #
        # 예: need = 4, box = 4
        if box == need:
            answer += 1

            # box번 상자를 트럭에 실었으므로
            # 메인 컨베이어는 다음 상자로 이동한다.
            box += 1

        # 메인 컨베이어 앞 상자가 need가 아니면
        # 보조 컨베이어 맨 위를 확인한다.
        #
        # stack[-1]만 꺼낼 수 있다.
        # stack 중간 값은 꺼낼 수 없다.
        elif stack and stack[-1] == need:
            stack.pop()
            answer += 1

        # 메인 컨베이어 앞 상자도 need가 아니고
        # 보조 컨베이어 맨 위도 need가 아니면
        # 더 이상 order 순서대로 실을 수 없다.
        else:
            break

    return answer
print(solution([4, 3, 1, 2, 5]))  # 2
print(solution([5, 4, 3, 2, 1]))  # 5