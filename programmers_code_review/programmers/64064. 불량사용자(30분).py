# 응모자 아이디 배열 user_id
# 불량사용자 이름 목록 banned_id
# 아이디 중 일부 문자 '*' 문자로 가려서 전달
# 문자 하나에 '*', 아이디당 최소 하나 이상 '*'
# 불량사용자 목록에 매핑된 응모자 아이디를 제재 아이디 -> 가려지지 않은 원본.
# 제재아이디 목록은 몇 가지 경우의 수가 가능한지 return
# 나열된 순서는 상관없이 하나로 카운트. 중복으로 제재아이디에 들어가는 경우는 없음
# 모든 불량 사용자 아이디 하나는 응모자 아이디에서부터 나옴.

# user_id에서 매칭하는 방법을 함수로 뺌. 로직이 길어서

# user 하나와 banned 하나만 비교하는 함수
def is_match(user, banned):
    # 문자열 길이가 다르면 애초에 불가능
    if len(user) != len(banned):
        return False

    for i in range(len(user)):
        if banned[i] == '*':
            continue
        if user[i] != banned[i]:
            return False
    return True

def solution(user_id, banned_id):
    # 구해야 하는 문제는 실제로 만들 수 있는 제재 아이디의 집합의 개수 <- 풀어야 할 문제를 명확히 정의.
    # 모든 banned의 후보 리스트
    candidates = []
    # 패턴별 후보를 생성하고
    for banned in banned_id:
        #현재 banned_id의 후보 리스트
        temp = []
        # user_id에서 비교해야 하는데.. 각 자리 문자를 비교해서 '*'를 제외하고는 일치해야 함
        for user in user_id:
            # user하나와 banned하나를 비교
            if is_match(user, banned):
                # 현재 banned 패턴 하나에 들어갈 수 있는 user들을 temp에 모음
                temp.append(user)
        #candidates에는 banned_id 각각의 후보 리스트들(user_id)이 순서대로 저장됨
        candidates.append(temp)

    # DFS로 하나씩 실제로 배정하는 과정이 필요함. .
    # 한번 선택한 user_id는 선택안하니까, 백트래킹 과정이 필요함.
    # candidates의 몇 번째 줄을 보고 있는지
    # 같은 user 중복 선택 방지
    answer_set = set()

    def dfs(idx, selected):
        # 모든 후보 줄을 다 봤으면 경우 하나 완성
        if idx == len(candidates):
            answer_set.add(tuple(sorted(selected)))
            return

        # idx번째 후보 줄에서 user 하나씩 보기
        for user in candidates[idx]:

            # 이미 고른 user면 건너뜀
            if user in selected:
                continue

            # user를 추가한 목록으로 다음 줄 탐색
            dfs(idx + 1, selected + [user])

    dfs(0, [])
    return len(answer_set)


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "abc1**"]
))
# expected: 2


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["*rodo", "*rodo", "******"]
))
# expected: 2


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"]
))
# expected: 3