# https://leetcode.com/problems/equal-sum-grid-partition-ii/?envType=daily-question&envId=2026-03-26
# 가로 한 줄: 맨 앞, 맨 뒤만 없앨 수 있음. 세로 한 줄: 맨 위, 맨 아래만 가능
# 2줄 이상~ 외곽 테두리 원소 + 가운데 아무 곳이나 상관 x

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        # 가로 분할
        top_sum = 0
        top_set = set()
        bottom_cnt = collections.Counter(v for row in grid for v in row)
        
        for i in range(m - 1):
            row_sum = 0
            for c in range(n):
                v = grid[i][c]
                row_sum += v
                top_set.add(v)
                bottom_cnt[v] -= 1

                if bottom_cnt[v] == 0:
                    del bottom_cnt[v]
                    
            top_sum += row_sum
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)
            b = [0, i] if top_sum > bottom_sum else [i + 1, m - 1] # 뺄 원소를 더 큰 쪽에서 찾기 위함

            if b[0] == b[1]: # 가로 한 줄
                if grid[b[0]][0] == diff or grid[b[0]][n-1] == diff: return True
            elif n == 1: # 세로 한 줄
                if grid[b[0]][0] == diff or grid[b[1]][0] == diff: return True
            else:
                if top_sum > bottom_sum:
                    if diff in top_set: return True
                else:
                    if diff in bottom_cnt: return True
        
        # 세로 분할
        left_sum = 0
        left_set = set()
        right_cnt = collections.Counter(v for row in grid for v in row)
        
        for j in range(n - 1):
            col_sum = 0
            for r in range(m):
                v = grid[r][j]
                col_sum += v
                left_set.add(v)
                right_cnt[v] -= 1
                if right_cnt[v] == 0:
                    del right_cnt[v]
                    
            left_sum += col_sum
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True
            
            diff = abs(left_sum - right_sum)
            b = [0, j] if left_sum > right_sum else [j + 1, n - 1] 

            if b[0] == b[1]: # 세로 한 줄
                if grid[0][b[0]] == diff or grid[m-1][b[0]] == diff: return True
            elif m == 1: # 가로 한 줄
                if grid[0][b[0]] == diff or grid[0][b[1]] == diff: return True
            else:
                if left_sum > right_sum:
                    if diff in left_set: return True
                else:
                    if diff in right_cnt: return True
                    
        return False

'''
# TLE

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        top_sum, bottom_sum = 0, total
        for i in range(m-1):
            target = sum(grid[i])
            top_sum += target
            bottom_sum -= target

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)
            b = [0, i] if top_sum > bottom_sum else [i+1, m-1]

            if b[0] == b[1]:
                if grid[b[0]][0] == diff or grid[b[0]][n-1] == diff:
                    return True
            elif n == 1:
                if grid[b[0]][0] == diff or grid[b[1]][0] == diff:
                    return True
            else:
                for r in range(b[0], b[1]+1):
                    if diff in grid[r]:
                        return True
        
        col = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        left_sum, right_sum = 0, total
        for i in range(n-1):
            left_sum += col[i]
            right_sum -= col[i]

            if left_sum == right_sum:
                return True
            
            diff = abs(left_sum - right_sum)
            b = [0, i] if left_sum > right_sum else [i+1, n-1]

            if b[0] == b[1]:
                if grid[0][b[0]] == diff or grid[m-1][b[0]] == diff:
                    return True
            elif m == 1:
                if grid[0][b[0]] == diff or grid[0][b[1]] == diff:
                    return True
            else:
                for r in range(m):
                    if diff in grid[r][b[0]:b[1]+1]:
                        return True
                    

        return False
'''
