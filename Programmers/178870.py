def solution(sequence, k):
    answer = []
    length = len(sequence)
    s = 0
    e = 0
    total = 0
    temp_max = 1000000000
    
    while e < length:
        total += sequence[e]
        e += 1
        
        if total > k:
            while total > k:
                total -= sequence[s]
                s += 1
        if total == k:
            if temp_max > (e - s - 1):
                temp_max = (e - s - 1)
                answer = [s, e - 1]
        
    
    return answer

'''
시간초과 풀이

def solution(sequence, k):
    answer = []
    window = 1
    
    while True:
        for i in range(len(sequence)):
            if sum(sequence[i:i+window]) == k:
                return [i, i+window-1]
        window += 1
        
    return answer

def solution(sequence, k):
    answer = []
    
    for i in range(len(sequence)):
        total = 0
        
        if sequence[i] == k:
            return [i, i]
        
        if i == len(sequence) or sequence[i] > k:
            break
            
        for j in range(i, len(sequence)):
            total += sequence[j]
            now_length = j - i
            
            if answer:
                if answer[-1][1] - answer[-1][0] < now_length:
                    break
                
            if total == k:
                answer.append([i, j])
                break
    
    answer.sort(key=lambda x: x[1] - x[0])
    
    return answer[0]
    
'''
