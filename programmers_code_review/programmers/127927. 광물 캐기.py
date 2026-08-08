from collections import deque

def split_minerals(picks, minerals):
    # 곡갱이로 캘 수 있는 광물 알아냄
    max_count = sum(picks) * 5
    minerals = minerals[:max_count]
    groups = []
    #광물을 5개씩 묶음
    for i in range(0, len(minerals), 5):
        groups.append(minerals[i:i+5])
    return groups

def count_minerals(group):
    diamond = group.count("diamond")
    iron = group.count("iron")
    stone = group.count("stone")
    return diamond, iron, stone
def get_group_score(diamond, iron, stone):
    return diamond * 25 + iron * 5 + stone

def get_fatigue(pick_type, diamond, iron, stone):
    if pick_type == 0:
        return diamond + iron + stone
    if pick_type == 1:
        return diamond * 5 + iron + stone
    if pick_type == 2:
        return diamond * 25 + iron * 5 + stone


def solution(picks, minerals):
    answer = 0
    groups = split_minerals(picks, minerals)
    group_infos = []
    for group in groups:
        diamond, iron, stone = count_minerals(group)
        score = get_group_score(diamond, iron, stone)
        group_infos.append([score, diamond, iron, stone])
    # 난도가 높은 그룹부터 나올 수 있도록 함.
    group_infos.sort(reverse=True)

    for score, diamond, iron, stone in group_infos:
        # 다이아, 철, 돌 순으로 배정함. 
        if picks[0] > 0:
            answer += get_fatigue(0, diamond, iron, stone)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += get_fatigue(1, diamond, iron, stone)
            picks[1] -= 1
        elif picks[2] > 0:
            answer += get_fatigue(2, diamond, iron, stone)
            picks[2] -= 1
    return answer

# empty = solution(picks, minerals)

print(solution([1,3,2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
))