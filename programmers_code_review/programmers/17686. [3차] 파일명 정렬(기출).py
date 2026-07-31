# 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.
#HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
#NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
#TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.
# 숫자를 포함한 정렬기능

def split_file(file):
    # file은 일단 스트링임.
    i = 0
    # isdigit()은 문자열이 숫자인지 검사하는 메서드. digit은 한글로 숫자 한자리.
    #인덱스가 파일길이 미만이면서, 해당 인덱스의 파일문자가 문자가 아니면
    while i < len(file) and not file[i].isdigit():
        i += 1
    # while문을 다 돌고 나면
    head = file[:i]
    j = i
    # 인덱스가 파일길이 미만이면서, 해당 인덱스의 파일문자가 숫자면
    while j <len(file) and file[j].isdigit():
        j += 1
    #숫자가 끝날때까지 while문을 다 돌고 나면
    number = file[i:j]
    # 소문자로 통일된 head와 number 정수를 반환한다.
    return head.lower(), int(number)


def solution(files):
    return sorted(files, key=lambda file: split_file(file))
    #숫자가 나타나기 전을 head라고 함
    #head기준 사전 순 정렬. 대소문자 구분 안함.
    # number 숫자순으로 정렬. 앞에 0이 있는거는 무시한다. 그냥 int로 생각한다.
    # 원래 입력에 주어진 순서를 유지한다.
    # 파일의 순서가 달라지지 않는다.
    #숫자 다음을 tail이라고 함.

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
