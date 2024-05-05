# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        l3 = dummy
        
        r = 0
        while l1 and l2:
            sumd = r + l1.val + l2.val
            r = sumd // 10
            q = sumd % 10
            l3.next = ListNode(q)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sumd = r + l1.val
            r = sumd // 10
            q = sumd % 10
            l3.next = ListNode(q)
            l3 = l3.next
            l1 = l1.next

        while l2:
            sumd = r + l2.val
            r = sumd // 10
            q = sumd % 10
            l3.next = ListNode(q)
            l3 = l3.next
            l2 = l2.next

        if r > 0:
            l3.next = ListNode(r)

        return dummy.next
             
        