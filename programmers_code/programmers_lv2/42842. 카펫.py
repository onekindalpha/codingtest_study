# yellow_width = 노란색이 가로로 몇 칸
# yellow_height = 노란색이 세로로 몇칸

def solution(brown, yellow):
    total = brown + yellow

    # 노란색 세로를 잡아보기.
    for yellow_height in range(1, yellow +1):
        # yellow = 노란색 가로 * 노란색 세로
        if yellow % yellow_height == 0:
            yellow_width = yellow // yellow_height

            brown_width = yellow_width + 2
            brown_height = yellow_height +2

            if brown_width >= brown_height and brown_width  * brown_height == total:
                return [brown_width, brown_height]
print(solution(10, 2))   # [4, 3]
print(solution(8, 1))    # [3, 3]
print(solution(24, 24))  # [8, 6]