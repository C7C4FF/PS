# https://school.programmers.co.kr/learn/courses/30/lessons/17680#

# 들어올 때 1, 캐시 안에 없으면 5
# 굳이 도시가 사용된 횟수를 같이 적을 필요는 없음
# LRU 알고리즘 : 사용된 캐시는 가장 뒤로 보내 최신화를 해줘야 함.

def solution(cacheSize, cities):
    answer = 0
    cities = [x.lower() for x in cities]
    stack = []
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        index = None
        
        if city in stack:
            index = stack.index(city)
            
        if index is not None:
            answer += 1
            stack.pop(index)
        else:
            answer += 5
            if len(stack) == cacheSize:
                stack.pop(0)
            
        stack.append(city)

    return answer
