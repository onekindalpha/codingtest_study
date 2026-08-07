import sys
from bisect import bisect_left
from stringprep import b1_set

input = sys.stdin.readline

# 산 높이의 최대값
# 문제/ 해설 기준으로 산 높이는 1이상 1,000,000 이하
MAX_H = 1_000_000
# 등산 이동 성공 또는 케이블카 이용 성공 시 얻는 점수 .
BONUS = 1_000_000

class SegmentTree:
    """
    세그먼트 트리 :
    이 트리는 "높이"를 기준으로 정보를 저장한다.

    저장하는 값
    (lis_length, last_height)

    lis_length:
    증가하는 등산 경로에서 방문한 산 개수

    last_height:
    그 경로의 마지막 산 높이

    비교 기준:
    1. lis_length가 큰 쪽이 더 좋다.
    2. lis_length가 같으면 last_height가 큰 쪽이 더 좋다.
    """
    def __init__(self):
        self.size = 1
        # 세그먼트 트리는 내부 크기를 2의 거듭제곱으로 맞춘다.
        while self.size < MAX_H:
            self.size *= 2
        #처음에는 아무 산도 없으므로 전부 (0, 0)
        self.tree = [[0, 0]] * (self.size * 2)
    def better(self, a, b):
        """
        a, b중 더 좋은 상태를 반환한다.
        a = (LIS길이, 마지막 산 높이)
        b = (LIS길이, 마지막 산 높이)
        """
        # LIS길이가 더 긴 쪽 선택
        if a[0] > b[0]:
            return a
        if a[0] < b[0]:
            return b
        # LIS 길이가 같으면 마지막 산 높이가 큰 쪽 선택
        if a[1] >= b[1]:
            return a
        return b
    def update(self, height, value):
        """
        특정 높이 height의 정보를 value로 갱신한다.
        height:
        산 높이, 이 값ㄷ을 그대로 세그먼트 트리 인덱스로 쓴다.
        value:
        (LIS길이, 마지막 산 높이)
        """
        # height는 1부터 시작한다고 보고 리프 위치로 변환
        idx = self.size + height -1
        # 리프 노드 갱신
        self.tree[idx] = value
        #부모 노드들 갱신
        idx //= 2
        while idx >= 1:
            self.tree[idx] = self.better(
                self.tree[idx *2],
                self.tree[idx *2 + 1]
            )
            idx //= 2
    def query(self, left, right):
        """
        높이 구간 [left, right]안에서 가장 좋은 상태를 찾는다.
        예:
        query(1, height-1)
        뜻:
        현재 산 높이보다 낮은 산들 중 LIS길이가 가장 긴 상태를 찾는다.
        왜 height -1까지 보나?
        등산 조건이 더 높은 산이기 때문.
        같은 높이는 이도 ㅇ불가.
        """
        #빈 구간이면 가능한 경로 없음
        if left > right:
            return (0, 0)
        # 리프 위치로 변환
        left = self.size + left -1
        right = self.size + right -1
        result = (0, 0)
        while left <= right:
            if left % 2==1:
                result = self.better(result, self.tree[left])
                left += 1
            if right % 2==0:
                result = self.better(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return result
class MountainGame:
    """
    전체 상태 관리 클래스.
    상태 1. mountains
    현재 산 높이 목록
    1-index로 관리하려고 앞에 0을 넣는다.
    상태 2. answer
    answer[i] = 1번 산부터 i번 산까지 봤을때, i번 산으로 끝나는 LIS길이.
    400번에서 케이블카 산 m까지 도달하는 LIS길이를 바로 꺼내기 위해 필요.
    상태 3. seg
    높이별 최고 LIS 상태를 저장하는 세그먼트 트리.
    상태4. restore_stack
    300번으로 오른쪽 산을 삭제할때, 세그먼트 트리를 이전 상태로 되돌리기 위한 스택

    """
    def __init__(self):
        self.seg = SegmentTree()
        #산 위치를 1번 부터 쓰기 위해 0번 칸은 버림
        self.mountains = [0]
        #answer[0]도 버림
        #삭제 복구용 스택
        self.restore_stack = []
    def reset(self, heights):
        """
        100번 퀴리: 빅뱅
        기존 상태를 전부 지우고,
        초기 산들을 왼족부터 차례대로 추가한다.
        """
        self.seg = SegmentTree()
        self.mountains = [0]
        self.answer = [0]
        self.restore_stack = []

        for height in heights:
            self.add_mountain(height)
    def add_mountain(self, height):
        """
        200번 쿼리: 산 추가
        산은 항상 오른쪽 끝에 추가된다.
        새 산 height로 끝나는 LIS를 계산한다.
        계산식: 현재 height보다 낮은 높이들 중 LIS최댓값 +1
        이유: 현재 산으로 오려면 이전 산 높이가 현재 산보다 낮아야 함.
        """
        #1. 나중에 삭제 복구를 위해 현재 height칸의 이전 상태 저장
        old_value = self.seg.query(height, height)
        self.restore_stack.append((height, old_value))
        #2. 현재 height보다 낮은 산들 중 가장 좋은 LIS상태 찾기
        best_lis_before, _ = self.seg.query(1, height-1)
        #3. 현재 산을 붙이면 길이가 1 증가
        current_lis = best_lis_before+1
        #4. 실제 산 목록에 추가
        self.mountains.append(height)
        #5. 이 위치 산으로 끝나는 lIS길이 저장
        self.answer.append(current_lis)
        #6. 세그먼트 트리에 현재 높이로 끝나는 lIS상태 저장
        self.seg.update(height, (current_lis, height))

    def remove_rightmost(self):
        """
        300번 퀴리: 가장 오른쪽 산 제거
        산은 오른쪽 끝에서만 제거 된다.
        그래서 마지막 add_mountain때 저장한 old_value로 복구하면 된다.
        """

        #산이 없으면 아무것도 안함
        if len(self.mountains) ==1:
            return

        # 실제 산 제거
        self.mountains.pop()
        #해당 위치의 LIS기록 제거
        self.answer.pop()
        #세그먼트 트리 이전 상태 복구
        height, old_value = self.restore_stack.pop()
        self.seg.update(height, old_value)
    def simulate(self, m_index):
        """
        400번 퀴리:등산 시뮬레이션 최대 점수
        m_index:케이블카가 있는 산의 위치
        문제에서 1-index로 주어진다.
        필요한 값:
        1. cable_lis = answer[m_index]
        1번 산부터 m_index번 산까지 봤을때, 케이블카 산까지 도착하는 lIS길이
        2. total_lis, final_height
        전체 산에서 가능한 LIS길이와 그 lIS중 마지막 산 높이가 가장 큰 값.

        점수 공식:
        ((total_lis -1) + cable_lis) * 1,000,000 + final_height

        왜 total_lis -1인가?
        LIS길이는 방문한 산 개수
        이동 성공 횟수는 산 개수보다 1 작음
        그래서 전체 LIS 이동 성공 점수는 (total_lis -1) * BONUS

        왜 cable_list는 그대로 더하나?
        케이블카 전: cable_lis 길이만큼 산을 방문했다면 이동 성공 횟수는 cable_lis -1
        케이블카 사용: +1회 성공
        합치면 : (cable_lis -1) + 1= cable_lis
        """
        total_lis, final_height = self.seg.query(1, MAX_H)
        cable_lis = self.answer[m_index]
        return ((total_lis -1) + cable_lis) * BONUS + final_height
def main():
    q = int(input())
    game = MountainGame()
    result = []
    for _ in range(q):
        data = list(map(int, input().split()))
        command = data[0]
        if command == 100:
            n = data[1]
            heights = data[2:]
            game.reset(heights)
        elif command == 200:
            height = data[1]
            game.add_mountain(height)
        elif command == 300:
            game.remove_rightmost()
        elif command == 400:
            m_index = data[1]
            result.append(str(game.simulate(m_index)))
    print("\n".join(result))

main()