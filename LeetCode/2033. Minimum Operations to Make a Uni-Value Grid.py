# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2026-04-28
# 최소 연산이 되려면 모든 원소를 중앙값으로 만들면 좋음
# 그러려면 각 원소와 중앙값의 차가 x의 배수여야 함 -> 그렇지 못하면 만들 수 없으므로 -1 반환

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ans = 0

        # 2중 리스트를 하나로 평면화한 뒤 정렬
        grid_flatten = [item for lst in grid for item in lst]
        grid_flatten.sort()

        median = grid_flatten[len(grid_flatten) // 2]   # 중앙값 찾기
        
        for num in grid_flatten:
            # 차이는 항상 x의 배수여야 함, x의 배수라면 나눈 몫만큼 더해주기
            diff = abs(median - num)
            if diff % x != 0:
                return -1
            else:
                ans += (diff) // x

        return ans

'''

# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2025-03-26
# 중간값에서 벗어날수록 연산이 많아짐 -> 연산 횟수를 최소한으로 만드려면 중간값으로 만들어야 함.
# 중간값은 절대 차의 합의 최소를 구할 때, 평균은 제곱 오차의 합의 최소를 구할 때

# 2차원 리스트를 단일 리스트로 만들기 위해서 itertools.chain(*list) or extend 로 이어주기
# 중간값을 구하기 위해서 정렬 -> 길이 // 2 로 중간값 구해주기
# 원래 배열의 원소와 중간값끼리의 절대값 차이인 배열을 만들어주고, 그 차이가 x의 배수인지 확인

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = list(chain(*grid))
        grid.sort()

        n = len(grid)
        median = grid[n // 2]
        
        gap = [abs(n-median) for n in grid]

        ans = 0
        for n in gap:
            if n % x == 0:
               ans += n // x
            else:
                return -1 

        return ans

'''
