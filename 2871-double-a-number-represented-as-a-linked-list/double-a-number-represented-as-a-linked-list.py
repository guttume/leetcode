# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        head = reverse(head)

        curr = head
        carry = 0
        dummy = ListNode()
        nh = dummy
        while curr or carry:
            val = curr.val if curr else 0
            p = (2 * val) + carry
            carry = p // 10
            value = p % 10
            nh.next = ListNode(value)
            nh = nh.next
            if curr:
                curr = curr.next

        return reverse(dummy.next)