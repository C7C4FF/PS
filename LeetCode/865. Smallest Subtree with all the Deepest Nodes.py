# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
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
