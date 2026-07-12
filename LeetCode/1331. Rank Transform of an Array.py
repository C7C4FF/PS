# https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2026-07-12
# 딕셔너리에 넣고 비교하기.. 

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        idx = {}
        ans = [0] * len(arr)
        sorted_arr = sorted(arr)

        now_max = float('-inf')
        rank = 0

        for i in range(len(arr)):
            if sorted_arr[i] > now_max:
                now_max = sorted_arr[i]
                rank += 1
                idx[sorted_arr[i]] = rank
            elif sorted_arr[i] == now_max:
                idx[sorted_arr[i]] = rank

        for i in range(len(arr)):
            ans[i] = idx[arr[i]]
        
        return ans
