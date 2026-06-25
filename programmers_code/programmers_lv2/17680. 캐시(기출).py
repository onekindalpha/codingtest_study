# cacheSize, cites
# 전자는 정수, 범위는 0 이상 30이하.
# 후자는 도시이름 문자열 배열, 최대 도시 수 100,000개이다.
# 각 도시 이름은 공백, 숫자, 특수문자 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20글자로 이루어져 잇다.
def solution(cacheSize, cities):
    answer = 0
    cache = []
    # 캐시 크기가 0이면 아무것도 저장할 수 없으므로 전부 miss
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        # 도시이름을 담는 리스트.
        # 앞쪽 오래된 것. 뒤쪽 최근에 사용한 것. pop이랑 append쓰려고
        if city in cache:
            # hit 이미 있어
            # answer은 지금까지 도시들을 처리하는 데 걸린 총 시간
            answer +=1
            # 방금 사용했으므로 가장 최근 위치로 이동
            cache.remove(city)
            cache.append(city)
        else:
            # miss 없어.
            answer += 5
        # 캐시가 꽉 찼으면 가장 오래된 것 제거.
            if len(cache) == cacheSize:
                cache.pop(0)
            # 새 도시를 캐시에 저장.
            cache.append(city)

    return answer

# 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다. 가장 오래 안쓴 것을 버린다.
# cache =  []
# 그 도시가 캐시 안에 있는지 본다.
# 있으면 hit -=> 시간 +1
# 없으면 miss  => 시간 +5
# 캐시가 꽉 찼으면 맨 앞 도시를 빼고, 새 도시를 맨 뒤에 넣는다.
# cache hit일 경우 실행시간은 1이다.
# cache miss일 경우 실행시간은 5이다.


print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# 50

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# 21

print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# 60

print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# 52

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# 16

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# 25