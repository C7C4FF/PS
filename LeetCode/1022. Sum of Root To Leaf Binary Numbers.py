# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/?envType=daily-question&envId=2026-02-24
# dfs 로 찾으면서 리프에 닿으면 더하기


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode], n: int) -> None:
            if not node:
                return
            
            n = node.val + 2 * n
            if not node.left and not node.right:
                self.ans += n
            
            dfs(node.left, n)
            dfs(node.right, n)
        
        dfs(root, 0)
        return self.ans
        
