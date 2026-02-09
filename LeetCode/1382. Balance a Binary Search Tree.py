# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder_sort = []
        self.inorder_traversal(root, inorder_sort)

        return self.bst(inorder_sort, 0, len(inorder_sort) - 1)

    def inorder_traversal(self, root: TreeNode, inorder: list):
        # 중위 순회
        if not root:
            return
        
        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)

    def bst(self, inorder: list, s: int, e: int) -> TreeNode:
        if s > e:
            return
        
        mid = s + (e - s) // 2

        left = self.bst(inorder, s, mid - 1)
        right = self.bst(inorder, mid + 1, e)

        node = TreeNode(inorder[mid], left, right)
        return node
