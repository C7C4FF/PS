# https://leetcode.com/problems/reverse-linked-list-ii/
# 1-based 명시되어 있지 않더라도 꼼꼼히 읽어보기..

# 1 2 3 4 5 | s = 1, e = 2
# 1 3 2 4 5 | s = 1, e = 2, tmp = 2
# 1 4 3 2 5 | s = 1, e = 2, tmp = 3
# 1 5 3 4 2 | s = 1, e = 2, tmp = 4
# 처럼 변경되도록... 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or right == left:
            return head

        root = start = ListNode()
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next
