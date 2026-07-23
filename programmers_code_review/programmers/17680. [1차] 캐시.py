# 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력함
# 캐시 교체 알고리즘은 LRU를 사용함
# cache_hit일 경우 실행시간은 1
# cache_miss일 경우 실행시간은 5

# 도시 이름을 하나씩 검색한다.
# 최근에 검색한 도시는 캐시에 저장된다.
# 같은 도시가 캐시에 있으면 빠르다.
# 캐시에 없으면 느리다.
# 총 실행시간을 구한다.

# 1. 도시 이름을 소문자로 바꾼다.
# 2. 캐시에 있으면:
#    - 실행시간 +1
#    - 기존 위치에서 지우고 맨 뒤에 넣는다.
# 3. 캐시에 없으면:
#    - 실행시간 +5
#    - 캐시가 꽉 찼으면 맨 앞 도시를 제거한다.
#    - 새 도시를 맨 뒤에 넣는다.

# 캐시 사이즈 = 캐시에 저장할 수 있는 개수
def solution(cacheSize, cities):
    answer = 0
    cache = []
    #캐시 크기가 0이면 아무 도시도 저장할 수 없다.
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cache:
            answer +=1
            # 기존 위치에서 지우고
            cache.remove(city)
            # 맨 뒤에 넣는다.
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            #새 도시를 맨 뒤에 넣는다.
            cache.append(city)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))