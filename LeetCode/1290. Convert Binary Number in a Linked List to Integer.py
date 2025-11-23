# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        lst = []

        while head != None:
            lst.append(head.val)
            head = head.next

        i = len(lst) - 1
        total = 0
        
        for binary in lst:
            
            total += binary * (2**i)
            i -= 1

        return total
