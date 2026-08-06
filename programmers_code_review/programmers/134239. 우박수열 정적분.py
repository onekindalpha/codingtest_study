
# 우박수열 구하기
def to_one(k):
    k_change = []
    n = 0
    #x가 0일때는 k이고
    x = 0
    k_change.append([x, k])
    #print(k_change)
    #x가 1일때부터 k값이 어떻게 바뀌는지
    while k != 1:
        if k % 2 == 0:
            k = k // 2
            n += 1
            x += 1
            #print("k가 짝수일때 한번 실행한 횟수", n)
            #print("k가 짝수면", k)
            k_change.append([x, k])
        else:
            k = k * 3 +1
            n += 1
            x += 1
            #print("k가 홀수일대 한번 실행한 횟수", n)
            #print("k가 홀수면", k)
            k_change.append([x, k])
        if k > 1:
            continue
    #print("k_change는", n, k_change)
    return n, k_change
#print("1이될때까지 횟수와 k_change는", to_one(k))

#정적분 구간 범위 구하기
def to_period(ranges, n):
    periods = []
    a = None
    b = None
    for i, value in enumerate(ranges):
        a = int(value[0])
        b = -int(value[1])
        #print(i, "번째 a, b는", a, b)
        #정적분 구간
        #y=0과 x=a, x=n-b로 둘러샇인
        period = [a, n-b]
        periods.append(period)
        #print(i, "번째 a, b는", period)
    #print("원소별 정적분 구간은", periods)
    return periods

# 1개 구간에 대한 정적분 넓이(=사다리꼴 넓이)구하기.
def make_squares(k_change, periods):
    # x=0에서 시작해서 구간별 누적으로 더할 사다리꼴의 넓이
    squares = []
    # 모든 k_change 원소의 정적분 결과
    results = []
    #한 k_change원소의 정적분 결과
    result = 0
    for i in range(len(k_change)-1):
        x0 = float(k_change[i][0])
        y0 = float(k_change[i][1])
        # 마지막 원소까지 사용됨. 그래서 i를 하나 작은것까지 범위로 해야 함.
        x1 = float(k_change[i+1][0])
        y1 = float(k_change[i+1][1])
        width = (x1-x0)
        height = (y0+y1)
        square = float((height * width) /2)
        squares.append(square)
        #print("x는",i, "에서", i+1, "까지 사다리꼴 넓이는", square)

    #print("구간별 사다리꼴 넓이는", squares)
    for period in periods:
        #print(period)
        start = int(period[0])
        end = int(period[1])
        if start > end:
            result = -1.0
            #이 부분이 문제였나
            results.append(result)
            continue
        # 아 여기서도 초기화해야지.
        result = 0.0
    # end앞까지는 :end까지로 함.
        for area in squares[start:end]:
            result += area
        #print(period, "에 대해 차례대로 정적 분 결과", result)
        # 전체 정적분 구간에 대한 정적분 결과를 담기 전에 초기화함.
        results.append(result)
        # 아 여기서 초기화를 해야 하는구나. 여기서 헤맸다.
        result = 0.0
    #print("모든 정적분 결과", results)
    return results
#make_squares(5, k_change)
#print(make_squares(k_change))

def solution(k, ranges):
    answer = []
    results = 0
    #우박수열을 구하고
    n, k_range = to_one(k)
        # 정적분 구간을 구하고
    periods = to_period(ranges, n)
        # 1개 구간의 사다리꼴 넓이를 구해서
    results = make_squares(k_range, periods)
        # 각 정적분 구간에 대한 사다리꼴 넓이 배열을 꾸하여 정답으로 한다.
        # 정적분 구간 배열 원소의 첫번째는 시작, 두번째는 끝이다. 이를 변수화한다.
    answer = results
    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
print(solution(3, [[0,0], [1,-2], [3,-3]]))