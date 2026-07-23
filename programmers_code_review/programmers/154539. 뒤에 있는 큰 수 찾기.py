# numbers 자신 뒤에 있는 중에서 나보다 크면서 가장 가까이에 있는것을 뒷큰수
# 뒷큰수가 없으면 -1
# 나보다 뒤에 있고, 나보다 크고, 가장 가까운수
# 현재 숫자가 앞에서 답을 기다리던 숫자들의 뒷큰수인지 확인한다.
# 왼족에서 오른쪽으로 하나씩 보니까, 나보다 처음으로 큰 숫자를 만나는 순간 바로 answer[idx]를 채우고 스택에서 뺌

def solution(numbers):
    answer = [-1] * len(numbers)
    # 나중에 넣은 것을 먼저 꺼내는 자료구조. 접시쌓기. LIFO.
    # stack[-1] 맨 위에 있는 것을 보는 것.
    # stack.pop. 스택 맨 위 값 꺼내기.
    # stack.append(x). push:스택에 넣기.
    stack = []
    # 왼쪽에서 오른쪽으로 각각 원소의 뒷 큰수를 찾아본다.
    # 뒷큰수를 찾으면 answer에 저장한다.
    for i in range(len(numbers)):
        # 스택이 비어있지 않고, 스택의 맨 위에 있는 것보다 현재 숫자가 큰 동안은 계속
        # 현재 숫자를 봤을 때,
        # 현재 숫자가 해결할 수 있는 인덱스를 계속 꺼낸다.
        # 꺼낸 인덱스는 다시 안들어간다. 최대 한번만 빠진다.
        while stack != [] and numbers[stack[-1]] < numbers[i]:
            # 스택의 맨 위 원소를 꺼낸다. 즉, 인덱스
            idx = stack.pop()
            # 그 인덱스의 뒷큰수를 현재 값이라고 변수를 저장한다.
            answer[idx] = numbers[i]
        # 스택에는 인덱스를 저장한다.
        stack.append(i)

    return answer

print(solution([2,3,3,5]))
print(solution([9,1,5,3,6,2]))

# 큐는 오래 기다린 인덱스부터 본다.
# 스택은 최근에 들어온 인덱스부터 본다.