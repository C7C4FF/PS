# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/?envType=daily-question&envId=2026-01-07
# 전체 합을 구하는 건 bfs 로 구하고.. dfs로 순회하면서 최댓값 갱신해주기
# 함수 내에서 갱신하기 1. nonlocal 선언 2. ans[0] 리스트로 만들기 3. self.ans 로 인스턴스 변수로 만들기

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_total_sum(self, root: Opional[TreeNode]) -> int:
        q = collections.deque([root])
        total = 0
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return total

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.total = self.get_total_sum(root)

        def dfs(node):
            if not node:
                return 0
            
            s = node.val + dfs(node.left) + dfs(node.right)
            self.ans = max(self.ans, (self.total - s) * s)

            return s
            
        dfs(root)
        
        return self.ans % (10**9 + 7)
