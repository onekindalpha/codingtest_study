# 서로 다른 토핑 수가 철수와 동생에게 공평하게 나눠지도록.
# 어떤 경우에는 공평하게 나누지 못할 수도 없음.

def solution(topping):
    answer = 0
    #왼쪽은 토핑 종류 수만 필요함
    left = set()
    #right = {1: 2, 2: 1, 3: 1}
    right = {}

    #처음에는 모든 토핑이 오른쪽에 있음
    for t in topping:
        # 토핑 t가 right이미 안에 있으면 개수 +1
        if t in right:
            right[t] +=1
        #토핑 t가 right안에 없으면 개수 1로 등록
        else:
            right[t] = 1
    # 토핑을 하나씩 왼쪽으로 옮김
    for t in topping:
        left.add(t)
        right[t] -= 1
        #토핑 개수가 0이 되면, 토핑종류를 지운다.
        if right[t] == 0:
            del right[t]
        if len(left) == len(right):
            #왼쪽 토핑 종류 수와 오른쪽 토핑 종류 수가 같으면 공평한 자르기
            answer += 1
# 철수가 먹는 토핑 개수 == 동생이 먹는 토핑 개수
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# 2

print(solution([1, 2, 3, 1, 4]))
# 0

print(solution([1, 2, 1, 3]))
# 1

print(solution([1, 1, 1, 1]))
# 3