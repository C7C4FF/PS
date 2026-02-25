# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# subsequence 라는 말에 속지 않기 > 어차피 큰 수 k 개를 뽑는 문제

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lst = []
        for i, value in enumerate(nums):
            lst.append((i, value))
        
        lst = sorted(lst, key=lambda x:x[1])[-k:]
        lst = sorted(lst, key=lambda x:x[0])
        
        ans = [v for i, v in lst]

        return ans
        
