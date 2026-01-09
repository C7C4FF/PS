# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            return 1 + max(get_depth(node.left), get_depth(node.right))
        
        max_depth = get_depth(root)
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return

            if depth == max_depth:
                return node
            
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)

            if left and right: 
                return node

            return left or right

        return dfs(root, 1)
        


'''
# 어제 했던 문제와 똑같은 문제

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return None, depth
            
            left, left_depth = dfs(node.left, depth + 1)
            right, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left, left_depth
            elif right_depth > left_depth:
                return right, right_depth
            else:
                return node, left_depth

        return dfs(root, 0)[0]
'''
