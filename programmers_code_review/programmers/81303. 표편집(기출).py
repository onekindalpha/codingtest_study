# 행 선택, 삭제, 복구하는 프로그램 작성
# 한번에 한 행만 선택가능.
# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다. 하나씩 뒤로 밀릴 수도 있네. 그 위에가 복구되면.

# 최종 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 "0", 삭제된 행은 "X"로 표시

# 처음 표의 행 개수를 나타내는 정수 n
# 처음에 선택된 행의 위치를 나타내는 정수 k
# 수행된 명령어들이 담긴 문자열 배열 cmd

# 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시하여 문자열 형태로 return

# 알고리즘 채택: 스택 + 연결리스트 + 구현

# U x: current를 prev방향으로 x번 이동
# D x: current를 next방향으로 x번 이동
# C: 현재 행 삭제, deleted에 현재 행 정보 저장, answer[current] = "X", 위 행과 아래 행을 서로 연결, current는 아래 행으로 이동, 아래 행 없으면 위 행으로 이동
# Z: deleted에서 최근 삭제 행 꺼냄. answer[꺼낸 행] = "O", 꺼낸 행을 위/아래 행 사이에 다시 연결

def solution(n, k, cmd):
    # 위 행/ 아래 행 연결
    # i번 행의 위 행
    prev = [i-1 for i in range(n)]
    # i번 행의 아래 행
    next = [i + 1 for i in range(n)]
    # 마지막 행 아래에는 아무 행도 없음
    next[n -1] = -1
    # 현재 선택된 행
    current = k
    deleted = []
    answer = ["O"] * n

    # cmd에서 하나씩 꺼내기
    for command in cmd:
        if command[0] == "U":
            x = int(command.split()[1])
            # 위로 x번 이동
            for _ in range(x):
                current = prev[current]
        elif command[0] == "D":
            x = int(command.split()[1])
            # 아래로 x번 이동
            for _ in range(x):
                current = next[current]
        elif command[0] == "C":
            #현재 행 삭제
            #삭제 복구할 때 3개가 필요함.
            before = prev[current] #현재 행 위에 있는 행
            after = next[current] #현재 행 아래에 있는 행
            deleted.append((current, before, after))

            # 삭제여부 저장
            answer[current] = "X"

            # 위 행과 아래 행 연결 -> 연결리스트의 핵심. 이어줘야 함.
                #이전 것의 다음 것은 after이고
            if before != -1:
                next[before] = after
                # 다음 것의 이전 것은 before이고
            if after != -1:
                prev[after] = before
            #current는 아래 행으로 이동
            if after != -1:
                current = after
            else:
                current = before
        # Z: deleted에서 최근 삭제 행 꺼냄. answer[꺼낸 행] = "O", 꺼낸 행을 위/아래 행 사이에 다시 연결
        elif command[0] == "Z":
            #최근 삭제 행 꺼냄. 가장 마지막 것이 나옴.
            row, before, after = deleted.pop()
            #삭제 여부 복구
            answer[row] = "O"

            #위 행과 다시 연결
            #이전것의 다음행을 row로
            if before != -1:
                next[before] = row
            #아래 행과 다시 연결
            #다음 것의 이전 행을 row로
            if after != -1:
                prev[after] = row

    return "".join(answer)


print(solution(
    8,
    2,
    ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
))
# 기대값: "OOOOXOOO"


print(solution(
    8,
    2,
    ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
))
# 기대값: "OOXOXOOO"


print(solution(
    5,
    0,
    ["C"]
))
# 기대값: "XOOOO"
# 0번 행 삭제


print(solution(
    5,
    4,
    ["C"]
))
# 기대값: "OOOOX"
# 마지막 행 삭제


print(solution(
    5,
    2,
    ["C", "Z"]
))
# 기대값: "OOOOO"
# 삭제 후 복구