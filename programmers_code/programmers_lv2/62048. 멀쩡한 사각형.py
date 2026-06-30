# 가로 W, 세로의 길이 H, 사용할 수 있는 정사각형의 개수
from math import gcd

def solution(w,h):
    total = w * h
    broken = w + h - gcd(w, h)
    return total - broken

print(solution(8, 12))
# 80