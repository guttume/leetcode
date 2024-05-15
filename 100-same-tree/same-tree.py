# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pa = []
        qa = []

        def iot(root, arr):
            if not root:
                arr.append(None)
                return None

            arr.append(root.val)
            iot(root.left, arr)
            iot(root.right, arr)

        iot(p, pa)
        iot(q, qa)

        print(pa)
        print(qa)

        pn = len(pa)
        qn = len(qa)

        if pn != qn:
            return False

        for i in range(pn):
            if pa[i] != qa[i]:
                return False

        return True