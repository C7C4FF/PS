# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/?envType=daily-question&envId=2026-04-27

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {
            1: [(0, -1), (0, 1)],   # 1: 왼쪽 - 오른쪽
            2: [(1, 0), (-1, 0)],   # 2: 위 - 아래
            3: [(0, -1), (1, 0)],   # 3: 왼쪽 - 아래
            4: [(0, 1), (1, 0)],    # 4: 오른쪽 - 아래
            5: [(0, -1), (-1, 0)],  # 5: 왼쪽 - 위
            6: [(0, 1), (-1, 0)],   # 6: 오른쪽 - 위
        }

        visited = set()
        def dfs(r, c):
            if r == m-1 and c == n-1:
                return True

            visited.add((r, c))

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc

                # 격자 안에 있고, 방문하지 않았으면 
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    connected = False
                    # 현재 위치로 돌아올 수 있는지 확인해야 함
                    for dnr, dnc in dirs[grid[nr][nc]]:
                        if nr + dnr == r and nc + dnc == c:
                            connected = True
                            break
                    
                    if connected:
                        if dfs(nr, nc):
                            return True
            
            return False

        return dfs(0, 0)
