# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return

            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

            ans.append(root.val)

        dfs(root)

        return ans