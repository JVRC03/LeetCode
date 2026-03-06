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
        q = deque([node])
        dic = {}
        vis = set()
        jvrc = deepcopy(q[0])

        while len(q):
            c = len(q)

            for i in range(c):
                n = q.popleft()

                if n not in dic:
                    dic[n] = []
                #print(type(n))
                if n is not None:
                    for child in n.neighbors:
                        if child not in vis:
                            q.append(child)
                            dic[n].append(child)
                            vis.add(child)
        return jvrc

        



