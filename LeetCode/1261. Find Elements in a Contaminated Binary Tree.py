# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/?envType=daily-question&envId=2025-02-21

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered = set()
        root.val = 0
        self.recover(root)

    def recover(self, node):
        self.recovered.add(node.val)
        if node.left:
            node.left.val = 2 * node.val + 1
            self.recover(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.recover(node.right)

    def find(self, target: int) -> bool:
        return target in self.recovered


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
