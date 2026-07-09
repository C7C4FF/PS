# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/?envType=daily-question&envId=2026-07-09
# 인접한 컴포넌트끼리 차이 확인해서 번호 부여
# 쿼리에서 두 인덱스가 동일한 컴포넌트를 가지고 있는지 확인

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        comp_no = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp_no += 1
            component[i] = comp_no
            
        return [component[u] == component[v] for u, v in queries]
