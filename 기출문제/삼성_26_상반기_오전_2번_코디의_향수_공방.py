from bisect import bisect_left

# 첫번째 줄에 작업의 수인 Q가 입력으로 주어짐
Q = int(input())
# 그 다음부터 Q개의 줄에 걸쳐 작업 정보가 입력으로 주어짐. 각 줄의 첫번째 정수는 작업의 종류를 나타냄. 뒤에 해당 작업의 인자가 따라옴
# 작업 한 줄을 정수로 변환하고,
# 첫 번째 값은 작업 종류, 나머지는 작업 인자로 분리함
for _ in range(Q):
    work_type, *args = map(int, input().split())
    if work_type == 1:
        N = args[0]
        #파이썬 인덱스와 향료번호(1~)를 맞추기 위해 0번 자리를 비움
        scents = [None] + args[1:]
    elif work_type ==2:
        new_scent = args[0]
        #향료추가하면
        scents.append(new_scent)
    elif work_type ==3:
        remove_idx = args[0]
        #향료 폐기하면
        #이미 폐기되었거나 존재하지 않는 번호인 경우
        # N은 처음에 추가된 향료의 개수니까, len(scents)로 구함.
        # 파이썬 인덱스는 리스트 마지막 인덱스가 len(scents)-1이다보니, 초과 아니고 이상으로
        if remove_idx >= len(scents) or remove_idx <= 0 or scents[remove_idx] is None:
            print(-1)
        #폐기전 향료 폐기를 출력함 (= 해당 향로의 향도를).
        else:
            print(scents[remove_idx])
        ## 폐기된 번호는 재사용되지 않는다고 하니, 실제로 삭제하는게 아니라 , None으로 넣어서 폐기를 표시함.
            scents[remove_idx] = None
    elif work_type ==4:
        blend_target = args[0]
        # 블렌딩이 수행될 때 출력함.
        # 일단 현재 사용가능한 향료에서 None빼고는 전부 불러와서 임시 리스트를 만든다.
        for_blend = []
        for scent in scents:
            if scent is not None:
                for_blend.append(scent)
        # 일단 리스트는 완성되었고, 합이 정확히 K가 되도록, 향료를 선택할 때, 향료 여러번 배치 가능, 필요한 향료의 초소 개수
        # 최소 개수만 구하면 되네
        # 내림차순으로 그리디는 최소 개수 보장 안함. 임의의 숫자 조합에서 큰 향료부터 선택하는거라.
        # 전체 sum으로는 임의의 조합으로 만들 수 있는지 판단할 수 없음.
        # DP로 풀어야 하는 이유: dp[x] = 합이 x가 되도록 만드는 최소 향료 개수
        # K를 만들려면 K보다 작은 중간 합들의 최소 개수가 필요하고, 그 중간 합도 다시 더 작은 합에 의존하기 때문
        INF = float('inf')
        #DP배열 크기 정하기. 최솟값 구하는 문제는 아주 큰 값으로 채움
        dp = [INF] * (blend_target + 1)
        #합 0은 향료를 하나도 사용하지 않으면 됨. 출발점을 정하기
        dp[0] = 0
        # 1부터 K까지의 합을 차례대로 계산. 작은 합부터 계산하기
        for i in range(1, blend_target + 1):
            for v in for_blend:
                # 향로의 향도가 현재 만들려는 합보다 작거나 같을때만 사용 가능
                # ex. i= 3, v=5이면 하나만으로 넘어버리니, 사용불가,
                if i >= v:
                    dp[i] = min(
                        # 지금까지 알아낸 현재 합을 만드는 데 필요한 최소 개수
                        dp[i],
                        # 낭믄 합 i-v를 만드는 데 필요한 최소 개수 + 지금 향로 V 1개
                        dp[i - v] + 1,
                    )
        #모든 계산이 끝난뒤 목ㅍ효 합을 만들 수 있는 지 확인한다.
        if dp[blend_target] == INF:
            print(-1)
        else:
            #목표합을 만들 수 있는 최소개수를 구한다.
            print(dp[blend_target])

    elif work_type ==5:
        composition_target = args[0]
        # 향수구성이 수행될 때 출력함.
        for_composition = []
        for scent in scents:
            if scent is not None:
                for_composition.append(scent)
        #이분탐색은 정렬된 배열에서만 사용가능하며, 오름차순으로 정렬해야 함.
        for_composition.sort()
        n = len(for_composition)
        answer = 0
        # top을 하나씩 선택한다.
        for top in for_composition:
            # mid를 하나씩 선택한다.
            for mid in for_composition:
                # top + mid + base가 composition_target 이상이어야 한다.
                # 따라서 base는 composition_target - top - mid 이상이어야 한다.
                need = composition_target - top - mid
                # 정렬된 향료 목록에서
                # 향도가 need 이상인 향료가 시작되는 인덱스를 찾는다.
                idx = bisect_left(for_composition, need)
                # idx부터 마지막 인덱스까지 있는 향료의 개수를 answer에 더한다.
                # 전체 개수 n - 시작 위치 idx
                answer += n - idx
        print(answer)
# 1번은 향료 준비(N, S1, ,,, Sn), 1번부터 N번까지 번호 부여, i번 향료의 향도는 Si임. 가장 처음에 한번만 주어짐.
# 2번은 향료 추가(v), 추가되는 향료의 번호는 순서대로 N+1, N+2, ...로 부여됨. 폐기된 번호는 재사용되지 않음. 새로 추가되는 향료의 향도는 v임
# 3번은 향료 폐기(idx), idx번 향료를 폐기함. 해당 향료의 향도를 출력함. 이미 폐기되었거나 존재하지 않는 번호라면 -1을 출력함
# 4번은 블렌딩(K), 현재 사용가능한 향료들 중에서 향도의 합이 정확히 K가 되도록 향료를 선택, 필요한 향료의 최소 개수, 같은 번호의 향료를 여러 번 사용할 수 있음, 만들 수 없다면 -1을 출려갛ㅁ
# 5번은 향수구성(K), 각 자리에 현재 사용가능한 향료를 하나씩 배치하여 향수를 구성, 세 향료의 향도의 합이 K이상이 되는 모든 경우의 수, 같은 번호의 향료를 여러 자리에 사용가능, 사용한 향료가 같더라도 배치한 자리가 다르면 서로 다른 경우임
# Q개의 작업이 순서대로 주어질 때, 각 작업에 대한 결과를 출력


