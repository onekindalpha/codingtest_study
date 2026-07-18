# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems
# 연속된 구간이어야 한다.
# 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return
# 만약 가장 짧은 구간이 여러개라면 시작 진열대 번호가 가장 작은 구간을 return
# 4종류의 보석(RUBY, DIA, EMERALD, SAPPHIRE) 8개
# gems 배열의 크기는 1이상 100,000이하임.
# gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있음
# gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열임
# 투 포인터/슬라이딩 윈도우 문제
# 모든 보석 종류가 들어 잇는 가장 짧은 연속 구간
# 아직 모든 종류가 없다 -> right를 움직여서 보석을 더 담는다
# 모든 종류가 들어왓다. -> 이제 left를 움직여서 앞쪽 보석을 빼며 구간을 줄인다.


def solution(gems):
    # 내가 반드시 모아야 하는 전체 보석 종류 수
    total_type_count = len(set(gems))
    # 현재 left부터 right까지 구간 안에 보석이 몇개씩 있는지 세는 딕셔너리. 현재 구간의 상태.
    gem_count = {}
    # 처음 구간은 0번 보석부터 시작한다.
    left = 0
    # 현재까지 찾은 가장 짧은 길이를 저장할 변수
    # 일부러 처음에는 큰 값으로 시작한다.
    shortest_length = len(gems) + 1
    # 임시 정답을 잡아두는데 처음에는 전체 구간을 정답이라고 대충 잡아둔다.
    answer = [1, len(gems)]
    # 오른쪽 손으로 보석 하나씩 담기
    # right는 for문이 자동으로 만들어줌. 0부터.
    for right in range(len(gems)):
        # 0번부터 마지막까지 하나씩
        gem = gems[right]
        # gem의 개수를 가져오고, 없으면 0으로 생각한다.
        # 이번에 보석을 하나 담았으니까 개수를 1개 늘린다.
        gem_count[gem] = gem_count.get(gem, 0) + 1

        # 만약 현재 left에서 right까지 구간의 보석 종류 수와 전체 보석 종류 수 가 같다면
        while len(gem_count) == total_type_count:
            # 현재 구간의 길이를 구한다.
            current_length = right - left +1
            # 만약 현재 길이가 최단 길이보다 짧다면, 현재 길이를 최단 길이로 한다.
            if current_length < shortest_length:
                shortest_length = current_length
                # 1번 진열대부터 진열하는 것이므로 +1로 바꾼다. 파이썬 인덱스는 0부터 시작하니까.
                answer = [left +1, right +1]

            # 여기서 left_gem을 정의한다.
            left_gem = gems[left]
            # 현재 구간에서 left_gem 보석을 하나 뺐다.
            gem_count[left_gem] -=1
            # 그 보석이 이제 하나도 없으면
            # 표에서 이름을 지운다.
            if gem_count[left_gem] ==0:
                del gem_count[left_gem]
            # left에 1을 하나씩 더한다.
            left += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [3,7]

print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1,3]

print(solution(["XYZ", "XYZ", "XYZ"]))
# [1,1]

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# [1,5]
