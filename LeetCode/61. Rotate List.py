# https://leetcode.com/problems/rotate-list/?envType=daily-question&envId=2026-05-05
# 연결리스트를 원형 리스트로 만들어주기
# k번 순회하는 건 원형 리스트의 총 길이로 나눠주면 그 나머지만큼만 이동하면 됨

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
            
        rotate = k % n
        tail.next = head

        new_tail = head
        for _ in range(n - rotate -1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None

        return new_head
        
        
