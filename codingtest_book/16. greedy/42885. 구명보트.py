# 정렬 + 투포인터 + 그리디
# 구명보트 문제
# 모든 사람을 구명보트로 구출해야 한다.
# 구명보트는 한 번에 최대 2명까지 탈 수 있다.
# 구명보트에는 무게 제한 limit이 있다.
# 목표는 필요한 구명보트 개수를 최소화하는 것이다.

# 그리디 판단
# 가장 무거운 사람은 어차피 보트 하나에 반드시 타야 한다.
# 가장 가벼운 사람과 같이 탈 수 있으면 같이 태운다.
# 가장 가벼운 사람과도 못 타면 누구와도 못 타므로 혼자 태운다.

# 풀이
# people을 오름차순 정렬한다.
# left는 가장 가벼운 사람, right는 가장 무거운 사람을 가리킨다.
# 두 사람이 같이 탈 수 있으면 left와 right를 모두 이동한다.
# 같이 못 타면 right만 이동한다.
# 매번 보트 개수를 1 증가시킨다.


def solution(people, limit):
    people.sort()

    left = 0
    right = len(people)-1
    boat = 0

    while left <= right:

        if people[left]+ people[right] <= limit:
            left += 1
        # 가장 무거운 사람은 무조건 태우기 때문
        # if문이 끝나면 아래로 내려감
        right -= 1
        boat += 1

    return boat

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))