"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = [node]
        if node:
            copies = {node: Node(node.val)}
        else:
            return None

        while q:
            cur = q.pop(0)

            for neigh in cur.neighbors:
                if neigh not in copies:
                    copies[neigh] = Node(neigh.val)
                    q.append(neigh)

                copies[cur].neighbors.append(copies[neigh])

        return copies[node]

            