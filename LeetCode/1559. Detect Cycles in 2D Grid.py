# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/?envType=daily-question&envId=2026-04-26
# 부모 노드가 아닌데 이미 방문했다면 사이클이 형성되었음

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [False] * (m * n)
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(r, c, pr, pc):
            visited[r * n + c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == grid[r][c]:
                    if (nr, nc) != (pr, pc):
                        if visited[nr * n + nc]:
                            return True
                        if dfs(nr, nc, r, c):
                            return True

            return False

        for i in range(m * n):
            r, c = i // n, i % n

            if not visited[i]:
                if dfs(r, c, -1, -1):
                    return True
            
        return False
