# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        l3 = dummy
        
        c = 0
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            c, value = divmod(c + v1 + v2, 10)
            l3.next = ListNode(value)

            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
             
        