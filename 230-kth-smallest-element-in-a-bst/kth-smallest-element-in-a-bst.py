# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def lot(root, ans):
            if not root:
                return None
            
            lot(root.left, ans)
            if root:
                ans.append(root.val)
            lot(root.right, ans)

        lot(root, ans)
        print(ans)
        return ans[k - 1]

