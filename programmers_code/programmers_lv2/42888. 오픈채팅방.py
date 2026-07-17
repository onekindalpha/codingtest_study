# 해시맵(dict) + 문자열 처리 + 2번 순회

def solution(record):
    name = {}

    for r in record:
        parts = r.split()
        cmd = parts[0]
        uid = parts[1]

        if cmd == "Enter" or cmd == "Change":
            nickname = parts[2]
            name[uid] = nickname

    answer = []

    for r in record:
        parts = r.split()
        cmd = parts[0]
        uid = parts[1]

        if cmd == "Enter":
            answer.append(name[uid] + "님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(name[uid] + "님이 나갔습니다.")

    return answer

print(solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


print(solution([
    "Enter uid1 A",
    "Change uid1 B",
    "Leave uid1"
]))
# ["B님이 들어왔습니다.", "B님이 나갔습니다."]


print(solution([
    "Enter uid1 A",
    "Enter uid2 B",
    "Change uid1 C",
    "Leave uid2"
]))
# ["C님이 들어왔습니다.", "B님이 들어왔습니다.", "B님이 나갔습니다."]