# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque

def bfs(matrix, visited, row, col):
    queue = deque([(row, col)])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[row][col] = True
    
    size = 0
    cols_set = set()
    
    while queue:
        r, c = queue.popleft()
        size += 1
        cols_set.add(c)
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(matrix) and (0 <= nc < len(matrix[0]))
                and matrix[nr][nc] == 1 and not visited[nr][nc]):
                visited[nr][nc] = True
                queue.append((nr, nc))
                
    return (size, cols_set)
    

def solution(land):
  '''
  oil = [(7, {3, 4, 5, 6}), (8, {0, 1, 2}), (2, {6, 7})]
  (해당 석유 덩어리의 총 크기, 접근 가능한 col들의 집합) 으로 만들어짐

  oil_rig = [8, 8, 8, 7, 7, 7, 9, 2]
  해당 열에 시추관을 꽂았을 때 얻을 수 있는 총 석유의 크기
  '''
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)] 
    oil_rig = [0] * m
    
    oil = []
    
    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and not visited[r][c]:
                this_size, this_cols = bfs(land, visited, r, c)
                oil.append((this_size, this_cols))
                
    for (size, cols) in oil:
        for col in cols:
            oil_rig[col] += size

        
    return max(oil_rig)
