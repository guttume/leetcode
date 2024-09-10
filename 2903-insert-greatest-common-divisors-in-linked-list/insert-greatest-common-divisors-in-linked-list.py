# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return abs(x)

        curr = head

        while curr.next:
            val = gcd(curr.val, curr.next.val)
            temp = curr.next
            node = ListNode(val, temp)
            curr.next = node
            curr = temp

        return head
            