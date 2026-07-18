# 숫자가 큰 쪽이 승리하게 되고, 승리한 사원이 속한 팀은 승점을 1점 얻게 됩니다.
#만약 숫자가 같다면 누구도 승점을 얻지 않습니다.
# A 팀원들이 부여받은 수가 출전 순서대로 나열되어있는 배열 A -> 이미 나와있음.
# i번째 원소가 B팀의 i번 팀원이 부여받은 수를 의미하는 배열 B
# B 팀원들이 얻을 수 있는 **최대 승점**. B가 최대한 많이 이기기.
# A와 B의 각 원소는 1 이상 1,000,000,000 이하의 자연수입니다
# 정렬 + 그리디 + 투 포인터
# 그리디: b가 a를 이길 수 있으면 가장 작은 카드로 이긴다. 못 이기면 제일작은 카드를 버린다.

# A배열은 이미 출전순서. B는 주어진 카드 목록으로 순서를 바꿀 수 있음.

def solution(A, B):
    # 작은 것부터 보려고 함. 보기 편하게.
    A.sort()
    B.sort()
    # result은 B의 최대 승점
    result = 0
    # 지금 이겨야 하는 A카드 위치와 지금 써볼 B카드 위치
    a_index = 0
    b_index = 0

    while a_index < len(A) and b_index < len(B):
        if B[b_index] > A[a_index]:
            result +=1
            a_index += 1
            b_index += 1
        else:
            b_index += 1

    return result

print(solution([5,1,3,7], [2,2,6,8]))
# 3
print(solution([2,2,2,2],[1,1,1,1]))
# 0