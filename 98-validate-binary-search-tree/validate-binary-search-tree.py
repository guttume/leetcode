# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, leftb, rightb):
            if not root:
                return True

            if not (leftb < root.val < rightb):
                return False

            return valid(root.left, leftb, root.val) and valid(root.right, root.val, rightb)

        
        return valid(root, float("-inf"), float("inf"))