# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/?envType=daily-question&envId=2026-01-06

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        level = 1
        ans = 0

        max_sum = float("-inf")

        while q:
            temp_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                temp_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if max_sum < temp_sum:
                max_sum = temp_sum
                ans = level
            
            level += 1
    
        return ans 

