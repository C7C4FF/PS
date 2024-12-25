class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def rightrootleft(node):
            if not node:
                return

            rightrootleft(node.right)
            self.sum += node.val
            node.val = self.sum

            rightrootleft(node.left)

        rightrootleft(root)
        return root
