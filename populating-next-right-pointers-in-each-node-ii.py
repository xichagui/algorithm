"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import queue


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = queue.Queue()
        if not root:
            return root
        q.put(root)
        q.put(None)
        cur = q.get()
        # flag = True
        while not q.empty():
            per = cur
            cur = q.get()
            if not per and not cur:
                break
            if per:
                per.next = cur
                if per.left:
                    q.put(per.left)
                if per.right:
                    q.put(per.right)
            else:
                q.put(None)
        
        return root
