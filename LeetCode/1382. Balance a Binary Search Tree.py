# https://leetcode.com/problems/balance-a-binary-search-tree/submissions/1913006582/?envType=daily-question&envId=2026-02-09
# inorder 순회로 트리의 정보를 다 얻은 뒤에 균형잡힌 이진트리로 만들기

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val_tree = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return None
            inorder(node.left)
            self.val_tree.append(node)
            inorder(node.right)

        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            
            m = (l + r) // 2
            node = self.val_tree[m]
            node.left = build(l, m - 1)
            node.right = build(m+1, r)

            return node
        
        inorder(root)
        balanced = build(0, len(self.val_tree) - 1)
        
        return balanced

'''
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
'''
