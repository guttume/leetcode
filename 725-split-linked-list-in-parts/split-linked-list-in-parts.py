# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Calculate the size of each part and how many parts need an extra node
        part_size = length // k
        extra_parts = length % k

        # Create the result list
        result = []
        curr = head
        
        for i in range(k):
            # Determine the size of the current part
            current_part_size = part_size + (1 if i < extra_parts else 0)
            
            if current_part_size == 0:
                result.append(None)
                continue
            
            # The start of the current part
            result.append(curr)
            
            # Advance to the end of the current part
            for _ in range(current_part_size - 1):
                if curr:
                    curr = curr.next
            
            # Split the current part from the rest of the list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        
        # If there are fewer parts than k, fill the remaining slots with None
        while len(result) < k:
            result.append(None)
        
        return result
        