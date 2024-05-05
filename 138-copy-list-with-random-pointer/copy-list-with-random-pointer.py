"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        curr = head
        while curr:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = temp

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        newh = head.next
        while curr:
            temp = curr.next.next
            if temp:
                curr.next.next = temp.next
            curr.next = temp
            curr = temp

        return newh

        

        