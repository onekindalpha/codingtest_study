# 2차원 벽면은 n x n 격자 형태이고, 구조물은 교차점 좌표를 기준으로 설치된다.
# build_frame의 각 명령은 [x, y, a, b] 형태다.
# x, y: 구조물을 설치/삭제할 교차점 좌표
# a: 구조물 종류, 0은 기둥, 1은 보
# b: 작업 종류, 0은 삭제, 1은 설치
# 따라서 build_frame을 순서대로 처리하는 시뮬레이션 문제다.

# 기둥은 (x, y)에서 위쪽으로 설치된다.
# 보은 (x, y)에서 오른쪽으로 설치된다.
# 현재 설치된 구조물은 (x, y, a) 형태로 저장한다.

# 핵심:
# 1. 명령을 일단 반영한다.
# 2. 현재 전체 구조물이 유효한지 검사한다.
# 3. 유효하지 않으면 방금 작업을 되돌린다.
# 4. 삭제는 다른 구조물의 조건을 깨뜨릴 수 있으므로 전체 유효성 검사가 필요하다.

def is_valid(structures):
    # 현재 설치된 모든 구조물이 자기 설치 조건을 만족하는지 검사한다.
    for structure in structures:
        x, y, a = structure

        # 기둥의 경우
        if a == 0:
            # 기둥은 자기 밑점 (x, y)가 받쳐져 있어야 한다.
            # 1. 바닥 위에 있거나
            # 2. 아래에 다른 기둥이 있거나
            # 3. 왼쪽에서 오는 보의 오른쪽 끝 위에 있거나
            # 4. 현재 좌표에서 오른쪽으로 뻗는 보의 왼쪽 끝 위에 있으면 유효하다.
            if (
                y == 0
                or (x, y-1, 0) in structures
                or (x-1, y, 1) in structures
                or (x, y, 1) in structures
            ):
                continue

            return False

        # 보의 경우
        if a == 1:
            # 보는 양 끝 중 하나가 기둥 위에 있거나,
            # 양쪽 끝이 다른 보와 동시에 연결되어 있어야 한다.
            # 보 (x, y, 1)의 왼쪽 끝은 (x, y), 오른쪽 끝은 (x+1, y)다.
            if (
                (x, y-1, 0) in structures
                or (x+1, y-1, 0) in structures
                or ((x-1, y, 1) in structures and (x+1, y, 1) in structures)
            ):
                continue

            return False

    return True


def solution(n, build_frame):
    # 현재 설치된 구조물들을 저장한다.
    # set을 쓰는 이유:
    # 1. 같은 구조물이 중복 저장되지 않는다.
    # 2. 특정 위치에 기둥/보가 있는지 빠르게 확인할 수 있다.
    structures = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)

        # 설치 명령
        if b == 1:
            # 일단 설치한다.
            structures.add(item)

            # 설치 후 전체 구조물이 유효하지 않으면 설치를 취소한다.
            if not is_valid(structures):
                structures.remove(item)

        # 삭제 명령
        else:
            # 일단 삭제한다.
            structures.remove(item)

            # 삭제 후 다른 구조물이 무너질 수 있으므로 전체 구조물을 다시 검사한다.
            # 유효하지 않으면 삭제를 취소한다.
            if not is_valid(structures):
                structures.add(item)

    # 문제에서 요구한 정렬 기준:
    # x 오름차순 → y 오름차순 → a 오름차순
    # 튜플 (x, y, a)는 sorted()가 이 순서대로 정렬한다.
    # 최종 반환은 튜플이 아니라 리스트 형태여야 한다.
    return [list(item) for item in sorted(structures)]


print(solution(5, [
    [1,0,0,1],
    [1,1,1,1],
    [2,1,0,1],
    [2,2,1,1],
    [5,0,0,1],
    [5,1,0,1],
    [4,2,1,1],
    [3,2,1,1]
]))