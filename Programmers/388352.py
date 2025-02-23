# https://school.programmers.co.kr/learn/courses/30/lessons/388352
# ans[i] = 0 은 사용하지 않으니 제거
# 모든 조합을 만들고, 돌면서 q[i] 와의 교집합이 ans[i] 와 모두 동일하다면 + 1

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    possible = list(range(1, n+1))
    removed = set()
    
    for lst, cnt in zip(q, ans):
        if cnt == 0:
            for i in lst:
                removed.add(i)
    
    possible = [i for i in possible if i not in removed]
    
    
    for combo in list(combinations(possible, 5)):
        flag = True
        
        for i in range(len(ans)):
            cnt = len(set(combo).intersection(set(q[i])))
            if cnt != ans[i]:
                flag = False
                break
        
        if flag:
            answer += 1
            

    return answer
