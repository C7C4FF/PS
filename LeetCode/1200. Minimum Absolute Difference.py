# https://leetcode.com/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26
# 더 낮은 diff 이 발견되면 ans를 비워줘야 함

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        n = len(arr)
        
        min_diff = 1e9
        for i in range(n - 1):
            diff = arr[i+1] - arr[i]

            if min_diff > diff:
                min_diff = diff
                ans = [[arr[i], arr[i+1]]] # ans 리스트 비우기

            elif min_diff == diff:
                ans.append([arr[i], arr[i+1]])
        
        return ans
         
