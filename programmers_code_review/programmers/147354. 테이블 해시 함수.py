
def to_sorted(data, col):
    sorted_data = sorted(data, key=lambda row: (row[col - 1], -row[0]))
    #print(sorted_data)
    rows = len(sorted_data)
    cols = len(sorted_data[0])
    return sorted_data, rows, cols

def make_S_i(sorted_data, rows, cols):
    #col은 1부터 data의 원소의 길이까지이다. 원소라는게 리스트 안의 리스트 형태인데...
    # i도 계산에 필요해서
    result = {}
    for i in range(1, rows + 1):
        S_i = 0
        #각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의해야 하는데.
        # 각 컬럼의 값................
        # 각 컬럼의 값을 i로 나눈 나머지들의 합으로 더한 총합.
        for j in range(1, cols + 1):
            extras = (sorted_data[i-1][j-1] % i)
            S_i += extras
        #print(i, "번째 튜플에 대한 S_i는", S_i)
        result[i] = S_i
        ##print(result)
    return result

def bitwiseXOR(sorted_data, row_begin, row_end, result):
    # 1보다 같거나 크고 rows보다 같거나 작은 범위에서
    # 0과 bitwiseXOR하면
    hased = 0
    # i가 있고, i에 해당하는 모든 S_i를 누적하여 bitwise XOR한 값을 해시값으로 반환
    #아래 세줄에서 틀렸음
    for i in range(row_begin, row_end+1):
        #print("범위는", row_begin, "에서", row_end, "까지")
        hased = hased ^ result[i]
        #print(hased)
    return hased

def solution(data, col, row_begin, row_end):
    answer = 0
    #1. 테이블 정렬하기 .
    sorted_data, rows, cols = to_sorted(data, col)
    #2. S_i를 정의하기.
    result = make_S_i(sorted_data, rows, cols)
    #3. row_begin <=i <= row_end인 모든 S_i를 누적하여 bitwise XOR한 값을 해시값으로서 반환
    answer = bitwiseXOR(sorted_data, row_begin, row_end, result)
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))
