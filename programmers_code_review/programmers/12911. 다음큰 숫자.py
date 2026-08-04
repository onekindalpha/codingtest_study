# 디버깅해서 풀었음.

def binary_count(num):
    binary_num = bin(num)
    binary_num = binary_num[2:]
    #print(binary_num[2:])
    one_count = binary_num.count("1")
    #print(one_count)
    return one_count
def solution(n): 
    answer = 0
    x = n + 1
    # #이건 넣어도 되나 모르겠네
    if x <= n:
        return False
    # 한번 하고 끝내게 해서는 안돼...
    while binary_count(n) != binary_count(x):
        x += 1
    answer = x
    return answer

print(solution(78))
print(solution(15))