# 개수만 세면 됨
import math
def solution(k, d):
    answer = 0
    dots = []
    # 좌표를 그려보면 x축과 y축의 최댓값은 d = ak 혹은 d = bk임.
    # a는 0부터 시작함.
    for a in range(d//k +1):
        x = a * k
        y_max = math.isqrt(d*d - x*x)
        # 몫 맞음. b는 양의 정수니까 소수점 아래는 버려야 함. 
        # b는 0부터 시작하니까 1추가
        b_max = y_max // k
        #print(b_max)
        #dots.append([a,b_max])
        #print(dots)
        answer += b_max + 1
    #print(answer)
    #answer = 0

    return answer
print(solution(2, 4))
print(solution(1, 5))