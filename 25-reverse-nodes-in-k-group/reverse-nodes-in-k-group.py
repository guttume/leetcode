# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(l):
            c = l
            p = None
            while c:
                t = c.next
                c.next = p
                p = c
                c = t
            return p

        def merge(l1, l2):
            if not l1:
                return l2
            c = l1
            while c.next:
                c = c.next
            c.next = l2
            return l1

        def count(l):
            c = l
            length = 0
            while c:
                c = c.next
                length += 1
            return length
            
        # break the list in to N/k parts
        heads = [head]
        c = head
        step = 1
        while c.next:
            c = c.next
            step += 1
            if step == k and c.next:
                heads.append(c.next)
                t = c.next
                c.next = None
                c = t
                step = 1

        # reverse each part only if lenght of each is k
        for i in range(len(heads)):
            if heads[i] and count(heads[i]) == k:
                heads[i] = reverse(heads[i])
        
        # merge each list into one
        ml = None
        for i in range(len(heads)):
            ml = merge(ml, heads[i])

        return ml