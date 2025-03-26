# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        # node.next 를 prev 에 이어줌
        # node = 2일 때 next는 3->4->5 가 되고, node.next가 1 -> None이 됨.
        # prev 는 2 -> 1 -> None 이 되고, node는 3 -> 4 -> 5 가 됨
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
    
        return prev
