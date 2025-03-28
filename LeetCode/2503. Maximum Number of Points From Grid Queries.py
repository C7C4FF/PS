# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/?envType=daily-question&envId=2025-03-28
# top-left 셀과 쿼리를 비교, queries[i] 보다 작으며, 인접한 곳들은 전부 방문하여 1점씩 획득
# bfs 로 순회하기
# 쿼리를 정렬하고 작은 순부터 차례대로 하면 한번의 순회로 다 구할 수 있음. -> 다시 원복해서 반환 값의 순서 맞추기

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        
        m = len(grid[0])
        n = len(grid)
        
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sorted_q = []
        for i, v in enumerate(queries):
            # 리스트로 볼 때는 아니어도, heappop으로는 최소힙으로 잘 꺼내짐
            heapq.heappush(sorted_q, [v, i])
            
        q = []
        cnt = 0 # 몇 개 가능한지 확인
        visited = [[False] * m for _ in range(n)]

        heapq.heappush(q, (grid[0][0], 0, 0))
        visited[0][0] = True

        for i in range(len(sorted_q)):
            value, index = heapq.heappop(sorted_q)

            while q and q[0][0] < value:
                cell, row, col = heapq.heappop(q)
                cnt += 1
                for dr, dc in d:
                    next_row, next_col = (row + dr, col + dc)

                    if (
                        next_row >= 0 and next_col >= 0
                        and next_row < n and next_col < m
                        and not visited[next_row][next_col]
                    ):
                        heapq.heappush(q, (grid[next_row][next_col], next_row, next_col))
                        visited[next_row][next_col] = True
                
            heapq.heappush(ans, [index, cnt])

        result = [pair[1] for pair in heapq.nsmallest(len(ans), ans)]
        return result
        
