# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(root, head):
            if not root:
                return False

            if root.val == head.val:
                if isMatch(root, head):
                    return True

            return dfs(root.left, head) or dfs(root.right, head)

        def isMatch(node, head):
            if not head:
                return True

            if not node or node.val != head.val:
                return False

            return isMatch(node.left, head.next) or isMatch(node.right, head.next)

        return dfs(root, head)

