# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=daily-question&envId=2026-06-14
# 연결 리스트를 전부 훑으면서 deque에 삽입. 그 이후 왼쪽과 오른쪽에서 각각 하나씩 빼면서 가장 큰 쌍을 구함

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = float('-inf')
        container = deque()

        node = head
        
        while node:
            container.append(node.val)
            node = node.next
        
        while container:
            s = container.popleft()
            e = container.pop()
            ans = max(ans, s+e)

        return ans
