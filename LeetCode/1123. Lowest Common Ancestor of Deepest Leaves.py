# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/?envType=daily-question&envId=2025-04-04

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            # node 가 None이면 리프노드에 도달함
            if not node:
                return None, depth
            
            # 현재 노드에서 왼쪽으로 돌며 lca-최소 공통 조상-를 구함
            left, left_depth = dfs(node.left, depth + 1)
            # 오른쪽으로 돌며 lca를 구함
            right, right_depth = dfs(node.right, depth + 1)
            
            # 왼쪽 오른쪽의 노드의 깊이가 같다면 해당 노드가 공통 조상임
            if left_depth == right_depth:
                return node, left_depth
            
            # 한쪽이 더 깊을 경우 깊은 쪽으로 반환
            return (left, left_depth) if left_depth > right_depth else (right, right_depth) 

        return dfs(root, 0)[0]
