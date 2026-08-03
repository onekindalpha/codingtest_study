
from math import lcm

def solution(arr):
    result = arr[0]

    for num in arr[1:]:
        result = lcm(result, num)

    return result

print(solution([2,6,8,14]))
print(solution([1,2,3]))