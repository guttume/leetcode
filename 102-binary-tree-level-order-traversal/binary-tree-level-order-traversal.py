# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()

        d = defaultdict(list)
        queue.append(root)
        level = 0
        d[level] = [root.val]
        level += 1
        while len(queue) > 0:
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                    d[level].append(root.left.val)
                if root.right:
                    queue.append(root.right)
                    d[level].append(root.right.val)
                
            level += 1
            
        ans = []
        for _, val in d.items():
            ans.append(val)

        return ans