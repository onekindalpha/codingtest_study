def solution(msg):
    # output = 압축 결과 번호 목록
    output = []

    # dic = 문자열 -> 번호
    dic = {}

    # 사전 초기화
    # A:1, B:2, ..., Z:26
    for num in range(1, 27):
        letter = chr(ord("A") + num - 1)
        dic[letter] = num

    # i = msg에서 처리 시작 위치
    i = 0

    # msg 끝까지 처리
    while i < len(msg):

        # w = 현재 위치 i에서 시작하는 문자열
        # 시작값은 한 글자
        w = msg[i:i+1]

        # j = msg[i:j]에서 끝 위치
        # j는 포함되지 않음
        j = i + 1

        # 사전에 있는 문자열을 찾기
        while j <= len(msg):

            # candidate = i부터 j 전까지 자른 문자열
            candidate = msg[i:j]

            # candidate가 사전에 있으면
            if candidate in dic:
                # w를 candidate로 갱신
                w = candidate

                # j를 1 증가시켜 다음 글자까지 포함
                j += 1

            # candidate가 사전에 없으면
            else:
                # 반복 종료
                break

        # w 번호를 output에 추가
        output.append(dic[w])

        # j <= len(msg)이면 candidate가 msg 범위 안에 있음
        # candidate는 사전에 없는 문자열
        if j <= len(msg):
            dic[msg[i:j]] = len(dic) + 1

        # 입력에서 w를 제거한 효과
        # 문자열 삭제 대신 i를 len(w)만큼 이동
        i = i + len(w)

    return output