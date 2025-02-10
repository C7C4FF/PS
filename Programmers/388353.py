# https://school.programmers.co.kr/learn/courses/30/lessons/388353

import re
from collections import deque

def solution(storage, requests):
    answer = 0
    
    n, m = len(storage), len(storage[0])
    
    def find_opened():
        opened = set()
        queue = deque()
        # 테두리(외부와 바로 인접한) 빈 칸들을 큐에 추가
        for i in range(n):
            for j in (0, m-1):
                if storage[i][j] == '.' and (i, j) not in opened:
                    opened.add((i, j))
                    queue.append((i, j))
        for j in range(m):
            for i in (0, n-1):
                if storage[i][j] == '.' and (i, j) not in opened:
                    opened.add((i, j))
                    queue.append((i, j))
                    
        while queue:
            i, j = queue.popleft()
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if storage[ni][nj] == '.' and (ni, nj) not in opened:
                        opened.add((ni, nj))
                        queue.append((ni, nj))
                        
        return opened
    
    for r in requests:
        temp = storage[:]
        
        if len(r) == 1:
            opened = find_opened()
            for i in range(n):
                f_iter = re.finditer(r, storage[i])
                
                for match in f_iter:
                    j = match.start()
                    # 테두리에 있을 경우
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        temp[i] = temp[i][:j] + '.' + temp[i][j+1:]
                    
                    # 상하좌우가 열려있는 곳일 경우
                    else:
                        if ((i-1, j) in opened or
                           (i+1, j) in opened or
                           (i, j-1) in opened or
                           (i, j+1) in opened):
                            temp[i] = temp[i][:j] + '.' + temp[i][j+1:]
                
        else:
            # 알파벳이 두개라면 해당 문자를 전부 없앰
            for i in range(n):
                temp[i] = re.sub(r[0], '.', temp[i])
            
        storage = temp

    for line in storage:
        for c in line:
            if c != '.':
                answer += 1
    
    return answer
