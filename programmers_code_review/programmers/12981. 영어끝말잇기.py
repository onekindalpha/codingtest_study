# tank → kick → know → wheel → land → dream → mother → robot → tank
# 사람의 수 n과 사람들이 순서대로 말한 단어 words가 매개변수로 주어짐.
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지
# 이미 말한 단어가 내 차례에 나오면 탈락임.

def solution(n, words):
    used_words = set()
    used_words.add(words[0])

    for index in range(1, len(words)):
        previous_word = words[index - 1]
        current_word = words[index]

        is_duplicate = current_word in used_words
        is_wrong_chain = previous_word[-1] != current_word[0]

        if is_duplicate or is_wrong_chain:
            person = index % n + 1
            turn = index // n + 1
            return [person, turn]

        used_words.add(current_word)

    return [0, 0]


# 테스트 1
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))  # [3, 3]


# 테스트 2
n = 5
words = [
    "hello", "observe", "effect", "take", "either",
    "recognize", "encourage", "ensure", "establish", "hang",
    "gather", "refer", "reference", "estimate", "executive"
]
print(solution(n, words))  # [0, 0]


# 테스트 3
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))  # [1, 3]