# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 우선 실행 순서: (), >, not, and, or
        # 헷갈릴 때는 괄호를 전부 넣자. if (not list1) or (list2 and (list1.val > list2.val)):
        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # temp 는 새 리스트노드의 끝을 가리키게 되고, ans 는 0부터 시작하는 헤드 다움부터 병합된 리스트 반환
        temp = ans = ListNode()

        while list1 and list2:
            # list2 가 크다면 list1 을 붙이고, list1이 크다면 list2 노드를 붙임
            if list2.val > list1.val:
                temp.next = list1
                list1, temp = list1.next, list1
            else:
                temp.next = list2
                list2, temp = list2.next, list2

        # 하나가 남았을 경우 나머지를 마저 이어줌
        if list1:
            temp.next = list1
        else:
            temp.next = list2

        return ans.next
'''
