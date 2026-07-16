# numbers
# numbers에 주어진 순서대로 하나의 이진트리로 해당 수를 표현할 수 있다면 1, 없다면 0
# 1차원 정수배열에 담아 return
# binary_arr = []
# dummy 노드 추가해 포화 이진트리로 만듦.
# 포화 이진트리의 왼쪽 노드부터 가장 오른쪽 노드까지, 왼쪽에 있는 순서대로 살펴봄
# 더미노드라면, 문자열 뒤에 0을 추가함. 더미노드가 아니라면 문자열 뒤에 1을 추가함
# 문자열에 저장된 이진수를 10진수로 변환함.

# 표현 가능한 이진트리: 이진수를 십진수로 변환
# 포화 이진트리 길이에 맞게 앞에 0을 채운다.
# 문자열의 가운데를 루트로 보고, (왜냐하면 포화이진트리로 맞추기 때문에)
# 부모가 0인데 자식 서브트리에 1이 있으면 불가능하다.
# 왼쪽/오른쪽 서브트리를 재귀로 검사한다.

# 이진수로 바꾸는 함수
def to_binary(number):
    return bin(number)[2:]
    #앞에 "0b"를 자르기 위해.
    #binary = 숫자를 이진수 문자열로 바꾼 것
# 포화 이진트리 길이로 만드는 함수
# 가장 작은 포화 이진트리는 노드 1개 짜리임.
def get_full_tree_length(binary_length):
    target_length = 1
    while binary_length > target_length:
        target_length = target_length * 2 + 1
    return target_length

# 포화 이진트리 길이에 맞게 앞에 0을 붙이는 함수
def make_full_binary(binary):
    binary_length = len(binary) # 지금 이진수 문자열 길이
    target_length = get_full_tree_length(binary_length) # 포화이진트리 길이
    zero_count = target_length - binary_length # # 포화 이진트리 길이에 맞추기 위해 앞에 붙일 0의 개수
    ## "0"을 zero_count번 반복해서 binary 앞에 붙인다.
    return "0" * zero_count + binary

# 포화이진트리 문자열이 문제 조건에 맞는지 검사하는 함수
def can_make_tree(binary):
    if len(binary)==1:
        return True
    mid = len(binary) // 2
    root = binary[mid]

    left = binary[:mid]
    right = binary[mid + 1:]
    # 부모노드가 0인데 자식노드가 1인 경우는 있을 수 없다.
    if root == "0" and ("1" in left or "1" in right):
        return False
    # 여기서 재귀를 사용. 왼쪽 서브트리도 검사, 오른쪼 서브리도 검사해서 둘다 가능해야 true임
    return can_make_tree(left) and can_make_tree(right)

def solution(numbers):
    answer = []

    for number in numbers:
        binary = to_binary(number)
        full_binary = make_full_binary(binary)
        if can_make_tree(full_binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer

# 프로그래머스 예시 테스트
print(solution([7, 42, 5]))      # [1, 1, 0]
print(solution([63, 111, 95]))   # [1, 1, 0]