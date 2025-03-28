# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# 단순 값 교환 - 변칙적인 풀이... (연결리스트 구조 상 next 포인터를 바꿔주는 게 필요함...)
# 반복이나 재귀로 풀기

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next

            head.next = self.swapPairs(p.next)
            p.next = head
            return p
            
        return head

'''
    # 단순 값 교환
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next # 다음 pair로

        return head
'''

'''
    # 반복
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head
      
        while head and head.next:
            # b가 a를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head # 오른쪽의 next를 왼쪽으로 이어줌

            # prev 가 b를 가리키도록 할당
            prev.next = b

            # 다음 쌍으로 이동
            head = head.next
            prev = prev.next.next

        return root.next
'''
