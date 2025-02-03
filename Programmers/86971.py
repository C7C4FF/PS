# https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    answer = []
    
    def union(a, b):
        a = find(a)
        b = find(b)
    
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
        
    def find(x):
        if parent[x] != x:
            return find(parent[x])
    
        return parent[x]
    
    for i in range(len(wires)):
        # 완전 탐색을 위해 해당 원소를 제외한 경우를 만듦
        new_wires = wires[:i] + wires[i+1:]
        
        parent = [i for i in range(n+1)]
        
        for a, b in new_wires:
            union(a, b)
        
        root = find(1)
        count = sum(1 for i in range(1, n+1) if find(i) == root)
        
        diff = abs((n - count) - count)
        answer.append(diff)
    
    return min(answer)
