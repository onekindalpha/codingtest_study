# 핵심 생각: 몸무게와 거리 곱한 것이 같으면 짝꿍인데
# 거리 는 3가지 경우 밖에 없다
# 가능한 거리 조합은 2-2, 3-3, 4-4, 2-3, 3-4, 2-4이다.
# 이때 몸무게의 비율을 생각하면 같은 몸무게끼리.
# 2-3일때는 몸무게 비율은 3:2
# 3-4일때는 몸무게 비율은 4:3
# 2-4일때는 몸무게 비율은 2:1임
# Counter는 리스트 안의 값이 몇번 나왔는지 세는 도구임
from collections import Counter
def solution(weights):
    answer = 0

    count = Counter(weights)
    # 몸무게 비율
    weight_ratios = [(1,2), (2, 3), (3, 4)]
    print(count)
    for weight, person_count in count.items():
        current_count = count[weight]
        print(weight, person_count)

    #같은 몸무게끼리 뽑는 코드.
        answer += current_count * (current_count-1) //2
        print(answer)
        #다른 몸무게끼리 뽑는 코드
        for small, large in weight_ratios:
            #몸무게로는 가벼운 사람이 먼거리, 무거운 사람이 가까운 거리에 앉ㅁ야 균형이 맞음.
            #ex. 180 : target = 2 : 3
            if weight * large % small == 0:
                target = weight * large // small
                if target in count:
                    #weight 몸무게 사람 수 × target 몸무게 사람 수
                    #= 두 몸무게 그룹 사이에서 만들 수 있는 짝 개수
                    answer += count[weight] * count[target]
    return answer
print(solution([100,180,360,100,270])) #4
#아래는 시간초과 난 코드.코드 구조를 새로 고쳤음.
# from collections import defaultdict
# from itertools import combinations
# def solution(weights):
#     #몸무게를 하나씩 꺼내기
#     #시소짝꿍을 찾기.
#     #distance중 하나랑 몸무게를 곱한 값이
#     distances = [2, 3, 4]
#     #번호별 가능한 거리를 다 넣어두고 싶으면
#     candidates = {}
#     #다른 사람이 distance중 하나랑 몸무게를 곱한 값이랑 같으면
#     # 균형을 이뤄서 시소 짝꿍이라고 함.
#     #왠지 인덱스도 필요할 것 같아서 enumerate()를 사용함.
#     for i, weight in enumerate(weights):
#         weight_distance_candidates = []
#         #첫번째 몸무게를 일단 꺼내서.
#         for distance in distances:
#             # 몸무게와 가능한 거리를 다 곱해봄.
#             weight_distance_candidates.append(weight*distance)
#         #가능한 거리들을 다 돌아봤으면 i인덱스별 후보들을 딕셔너리에 넣음.
#         candidates[i] = weight_distance_candidates
#     #그럼 이제 웨이트별로 가능한 weight_distance들이 쭉 있을텐데,
#     #같은 것끼리 딕셔너리에서 뽑아서 시소짝꿍을 만들려고 함
#     #value 리스트 안의 원소를 기준으로, 같은 원소를 가진 key들을 모으는 것
#     ## value를 기준으로 key들을 모을 딕셔너리
#     # 예: 2 -> ["a", "b", "c"]
#     # defaultdict(list)는 없는 key를 만나면 자동으로 []를 만든다
#     groups = defaultdict(list)
#     # key = "a", values = [1, 2, 3] 형태로 꺼낸다
#     for key, values in candidates.items():
#         # values 안에 같은 값이 여러 번 있을 수 있으므로 set(values)를 사용한다
#         # 예: "a": [1, 1, 2]이면 1 때문에 "a"가 두 번 들어가는 것을 막는다
#         for value in set(values):
#             # value를 가진 key를 groups[value]에 저장한다
#             groups[value].append(key)
#     # 최종 pair 중복 제거용 set
#     # 예: ("a", "c")가 1에서도 나오고 2에서도 나오면 한 번만 남긴다
#     pair_set = set()
#     # value별로 모인 keys를 확인한다
#     for value, keys in groups.items():
#
#         # 같은 value를 가진 key가 2개 이상일 때만 pair를 만들 수 있다
#         if len(keys) <2:
#             continue
#         # # keys 중에서 2개씩 조합을 만든다
#         for pair in combinations(keys, 2):
#             #pairs를 set에 넣어서 중복 pair를 제거한다.
#             pair_set.add(pair)
#     #보기 좋게 리스트로 바꾼다.
#     result = list(pair_set)
#
#     return len(pair_set)
#
#
# print(solution([100,180,360,100,270])) #4