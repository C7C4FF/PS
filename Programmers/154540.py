# https://school.programmers.co.kr/learn/courses/30/lessons/154540


from collections import deque

def bfs(matrix, visited, row, col):
    queue = deque([(row, col)])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[row][col] = True
    
    days = 0
    
    while queue:
        r, c = queue.popleft()
        days += int(matrix[r][c])
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(matrix) and (0 <= nc < len(matrix[0]))
                and matrix[nr][nc] != "X" and not visited[nr][nc]):
                visited[nr][nc] = True
                queue.append((nr, nc))
    
    return days

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    island = []
    
    for r in range(n):
        for c in range(m):
            if maps[r][c] != "X" and not visited[r][c]:
                days = bfs(maps, visited, r, c)
                island.append(days)

    if island:
        island.sort()
        return island
    else:
        return [-1]
