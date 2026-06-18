# 출발지점부터 도착지점까지 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n
# 바위 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return
# ex. distance = 25, rocks = [2, 14, 11, 21, 17], n=2
# 정확히 정답이 뭔지는 모르겠는데, 어떤 숫자 X를 줬을 때 이 X는 가능한가? 를 판단할 수 있으면 binary search 의심.
# 바위 사이의 최소 거리를 X 이상으로 만들 수 있는가?
def solution(distance, rocks, n):
    answer = 0

    # 바위를 위치 순서대로 확인해야 하므로 정렬
    rocks.sort()
    # 도착 지점도 마지막 지점으로 보고 거리 계산에 포함
    rocks.append(distance)

    # 만들고 싶은 최소 거리의 후보 범위
    left =1
    right = distance

    while left <= right:
        mid = (left + right) //2

        # ex. distance = 25, rocks = [2, 11, 14, 17, 21, 25], X=4라고 가정. prev(마지막으로 남긴 지점) =0
        # mid 거리 이상을 만들기 위해 제거해야 하는 바위 수
        removed = 0
        # 마지막으로 남긴 지점
        prev =0

        for rock in rocks:
            if rock - prev < mid:
                removed +=1
            else:
                prev = rock
        # 제거해야 하는 바위 수가 허락된 n개 이하라면
        if removed <= n:
            # mid는 가능한 거리
            answer = mid
            # 더 큰 최소 거리도 가능한지 확인
            left = mid + 1
        else:
            # mid거리 이상 만들려면 바위를 너무 많이 제거해야 함.
            # 목표 거리를 줄인다.
            right = mid -1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
# 4