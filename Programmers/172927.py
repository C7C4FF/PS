# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    answer = 0
    
    total = sum(picks)
    fatigue = []
    
    for i in range(total):
        mineral = minerals[i*5 : i*5 + 5]
        cost = 0
        if mineral:
            for m in mineral:
                if m == "diamond":
                    cost += 25
                elif m == "iron":
                    cost += 5
                else:
                    cost += 1
                    
            fatigue.append([mineral, cost])
    
    fatigue.sort(key=lambda x:x[1])
    
    while fatigue:
        mineral, cost = fatigue.pop()
        
        if picks[0]:
            answer += len(mineral)
            picks[0] -= 1
            
        elif picks[1]:
            for m in mineral:
                if m == "diamond":
                    answer += 5
                else:
                    answer += 1
            picks[1] -= 1
        else:
            answer += cost
            picks[2] -= 1
    
    
    
    return answer

# 다이아 > 철 > 돌, 기본적으로 하나 캘 때마다 1씩
# 자신보다 높은 등급을 캘 때는 단계 별로 x5 의 피로도가 듦
# 한 번 사용한 곡괭이는 5개를 캘 때까지 고정

# 돌 곡괭이를 기준으로 광물마다 25, 5, 1의 피로도를 가진다고 생각하고
# 피로도가 가장 높은 순서부터 (가능하면) 다이아몬드 곡괭이를 사용하고, 가장 낮을 때 돌 곡괭이를 사용
