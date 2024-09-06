# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = set()

        for n in nums:
            s.add(n)

        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            temp = curr.next
            if curr.val in s:
                curr.next = None
                prev.next = temp
            else:
                prev = curr
            curr = temp

        return dummy.next
            
