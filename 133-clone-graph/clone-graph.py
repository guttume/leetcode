"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        created = {}

        def dfs(node):
            if node.val in created:
                return created[node.val]

            newNode = Node(node.val)
            created[node.val] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
                
            return newNode

        return dfs(node)