# 의벤트 응모자 아이디 목록이 담긴 배열 user_id
# 불량사용자 목록에 매핑된 응모자 아이디를 제재 아이디라고 함. (banned_id하나하나에 user_id 중 하나를 붙여야 한다)
# 아이디 일부 문자를 '*' , 아이디 당 최소 하나 이상의 '*' 문자를 사용함.
# 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없다.
# 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return 하도록
# user_id 배열의 크기는 1 이상 8 이하입니다.
# banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하입니다.
# 순서와 관계없이 아이디 목록 내용이 동일하다면 같은 것으로 처리하여 하나로 셈.
# 백트래킹 / 완전탐색 + 집합 중복 제거 문제
# 풀이방법
# 1. 각 banned_id마다 매칭 가능한 user_id 후보를 찾는다.
def solution(user_id, banned_id):
    candidate_list = []
    def is_match(user, banned):
        # 길이가 다르면 넘어감.
        if len(user) != len(banned):
            return False
        for index in range(len(user)):
            # * 이 나오면 그 자리만 넘어감.
            if banned[index] == "*":
                continue
                # 믄지열이 다르면 그 user는 후보에서 탈락
            if user[index] != banned[index]:
                return False
        return True
    # 2. 각 banned_id마다 매칭 가능한 user_id 후보를 찾는다.
    for banned in banned_id:
        candidates = []

        for user in user_id:
            if is_match(user, banned):
                candidates.append(user)
        candidate_list.append(candidates)
    # 완성된 제제 아이디목록을 저장한다. 중복이 없는 set로 저장한다.
    result_set = set()
    # 3-1. 후보중에서 하나씩 골라본다.
    # 3-2. 이때, 이미 고른 user_id는 다시 고르지 않는다.
    # banned_index번째 불량아이디를 처리중이다.
    # 그 불량아이디에 들어갈 수 있는 user후보들을 하나씩 본다.
    def dfs(banned_index, selected_users):
        if banned_index == len(banned_id):
            # 순서와 관계없이 아이디 목록 내용이 동일하다면 같은 것으로 처리한다.
            result_set.add(tuple(sorted(selected_users)))
            return
        # 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없다.
        for user in candidate_list[banned_index]:
            if user in selected_users:
                continue
            selected_users.add(user)
            dfs(banned_index +1, selected_users)
            selected_users.remove(user)
    # 4. 끝까지 다 골랐으면 하나의 제재 목록이 완성된다.
    # 5. 같은 목록은 순서가 달라도 하나로 세야 하니까 set에 저장한다.

    # dfs 시작
    # 0번째 banned_id부터 시작하고, 아직 고른 user은 없으니까 빈 set으로 시작.
    dfs(0, set())
    # 중복 제거된 제재 아이디 목록 개수 반환
    return len(result_set)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
#2

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# 2

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# 3