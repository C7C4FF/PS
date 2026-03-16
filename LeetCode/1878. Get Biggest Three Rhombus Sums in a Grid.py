# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/?envType=daily-question&envId=2026-03-16
# 모든 합을 최대 힙에 넣고, 그 중 3개를 뽑기. 중복은 건너뛰기

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        self.max_heap = []
        self.m, self.n = len(grid), len(grid[0])

        def get_rhombus(grid: List[List[int]], m_coord: int, n_coord: int) -> None:
            length = min(abs((self.n-1) - n_coord), n_coord, abs((self.m-1) - m_coord), m_coord) # 보더라인까지 가장 짧은 길이, 그 길이만큼 반복할 예정

            while length >= 0:
                if length == 0: # 해당 좌표의 값
                    heapq.heappush(self.max_heap, -grid[m_coord][n_coord])
                else:
                    rhombus_sum = 0
                    x, y = m_coord - length, n_coord # 마름모의 위 좌표
                  
                    repeat = length
                    while y > 0 and repeat > 0: # 왼쪽 아래로 진행
                        rhombus_sum += grid[x][y]
                        x += 1
                        y -= 1
                        repeat -= 1

                    repeat = length
                    while (self.m - 1) > x and repeat > 0: # 오른쪽 아래로 진행
                        rhombus_sum += grid[x][y]
                        x += 1
                        y += 1
                        repeat -= 1

                    repeat = length
                    while (self.n - 1) > y and repeat > 0: # 오른쪽 위로 진행
                        rhombus_sum += grid[x][y]
                        x -= 1
                        y += 1
                        repeat -= 1

                    repeat = length
                    while x > 0 and repeat > 0: # 왼쪽 위로 진행
                        rhombus_sum += grid[x][y]
                        x -= 1
                        y -= 1
                        repeat -= 1

                    heapq.heappush(self.max_heap, -rhombus_sum)

                length -= 1 # 가능한 모든 마름모 체크

        for i in range(self.m):
            for j in range(self.n):
                get_rhombus(grid, i, j)
        
        ans = []
        while self.max_heap and len(ans) < 3:
            target = -heapq.heappop(self.max_heap)
            if not ans or target != ans[-1]:
                ans.append(target)

        return ans
