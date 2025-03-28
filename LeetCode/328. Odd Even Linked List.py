# https://leetcode.com/problems/odd-even-linked-list/

# 공간복잡도 O(1), 시간복잡도 O(n) 안에 해결
# 처음 두칸씩 건너 뛰면서 현재 가리키는 odd, even 옮겨주기
# val과는 상관 없이, 순서의 홀수 짝수만을 생각

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head # 홀수 노드의 마지막을 짝수 헤드로 연결
        return head
