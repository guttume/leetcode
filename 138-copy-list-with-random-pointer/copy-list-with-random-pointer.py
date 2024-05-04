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
        maph = {}

        curr = head

        while curr:
            maph[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        newh = maph[curr]
        neww = newh
        while curr.next:
            neww.next = maph[curr.next]
            if curr.random:
                neww.random = maph[curr.random]
            curr = curr.next
            neww = neww.next
        
        if curr.random:
                neww.random = maph[curr.random]

        return newh

        