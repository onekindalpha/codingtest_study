import math
from math import sqrt
from math import ceil
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        y_max = int(math.sqrt(r2*r2 - x*x))
        if x < r1:
            y_min = ceil(sqrt(r1*r1 - x*x))
        else:
            y_min = 0
        #끝값 - 시작값 +1
        answer += (y_max - y_min) +1
    return answer * 4
print(solution(2,3))