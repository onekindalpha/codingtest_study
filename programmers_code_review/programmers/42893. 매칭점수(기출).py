# 아래와 같은 규칙으로 검색어에 대한 웹페이지의 매칭점수를 계산
# 기본점수는 해당 웹페이지 텍스트 중 검색어가 등장하는 횟수(대소문자 무시)
# 외부 링크 수는 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수
# 링크점수는 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본 점수 나누기 외부 링크 수의 총합
# 웹페이지의 매칭점수는 기본점수와 링크점수의 합

# 검색어 word와 웹페이지 html 목록인 pages가 주어졌을때 매칭점수가 가장 높은 웹페이지의 index구하기
# 만약 여러개라면 그중 번호가 가장 작은 것을 구하기.

# 웹페이지의 index는 pages 배열의 index와 같으며 0부터 시작한다.

# 문자열 파싱 + 해시맵 + 점수 계산

import re

def solution(word, pages):
    urls = []
    base_scores = []
    links_list = []

    # 1. 각 page에서 필요한 정보 뽑기
    for page in pages:
        url = get_url(page)
        base_score = get_base_score(page, word)
        links = get_links(page)

        urls.append(url)
        base_scores.append(base_score)
        links_list.append(links)

    # 2. URL -> index 만들기
    url_to_index = {}

    for i in range(len(urls)):
        url_to_index[urls[i]] = i

    # 3. 링크 점수 계산
    link_scores = [0] * len(pages)

    for i in range(len(pages)):
        outgoing_links = links_list[i]

        if len(outgoing_links) == 0:
            continue

        score_to_give = base_scores[i] / len(outgoing_links)

        for link in outgoing_links:
            if link in url_to_index:
                target_index = url_to_index[link]
                link_scores[target_index] += score_to_give

    # 4. 매칭 점수 계산
    answer = 0
    max_score = -1

    for i in range(len(pages)):
        matching_score = base_scores[i] + link_scores[i]

        if matching_score > max_score:
            max_score = matching_score
            answer = i

    return answer


def get_url(page):
    matched = re.search(r'<meta property="og:url" content="(https://[^"]+)"', page)
    return matched.group(1)


def get_links(page):
    return re.findall(r'<a href="(https://[^"]+)"', page)


def get_base_score(page, word):
    word = word.lower()
    page = page.lower()

    # 알파벳이 아닌 문자를 공백으로 바꾸고, 공백 기준으로 나눈다.
    words = re.sub(r'[^a-z]', ' ', page).split()

    count = 0

    for w in words:
        if w == word:
            count += 1

    return count

def run_tests():
    # 테스트 1: 링크 점수 때문에 1번 페이지가 이김
    word1 = "blind"
    pages1 = [
        '''
        <html>
        <head>
            <meta property="og:url" content="https://a.com"/>
        </head>
        <body>
            blind blind
            <a href="https://b.com">link</a>
        </body>
        </html>
        ''',
        '''
        <html>
        <head>
            <meta property="og:url" content="https://b.com"/>
        </head>
        <body>
            blind
        </body>
        </html>
        '''
    ]

    assert solution(word1, pages1) == 1
    print("test 1 passed")

    # 테스트 2: 동점이면 index 작은 페이지
    word2 = "target"
    pages2 = [
        '''
        <html>
        <head>
            <meta property="og:url" content="https://site0.com"/>
        </head>
        <body>
            target
        </body>
        </html>
        ''',
        '''
        <html>
        <head>
            <meta property="og:url" content="https://site1.com"/>
        </head>
        <body>
            target
        </body>
        </html>
        '''
    ]

    assert solution(word2, pages2) == 0
    print("test 2 passed")

    # 테스트 3: 단어 단위 확인
    word3 = "blind"
    pages3 = [
        '''
        <html>
        <head>
            <meta property="og:url" content="https://x.com"/>
        </head>
        <body>
            blind blindxxx blind. BLIND, abcblind
        </body>
        </html>
        ''',
        '''
        <html>
        <head>
            <meta property="og:url" content="https://y.com"/>
        </head>
        <body>
            nothing
        </body>
        </html>
        '''
    ]

    assert solution(word3, pages3) == 0
    assert get_base_score(pages3[0], word3) == 3
    print("test 3 passed")

    print("all tests passed")


run_tests()