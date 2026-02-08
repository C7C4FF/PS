# https://leetcode.com/problems/balanced-binary-tree/description/?envType=daily-question&envId=2026-02-08
# 좌우 노드의 높이차가 2 이상이라면 균형 x

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.ans = False
            
            return 1 + max(left, right)
        
        dfs(root)

        return self.ans
