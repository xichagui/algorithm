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
        if not root:
            return root
        
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            cur = None
            for i in range(size):
                temp = q.get()
                if cur:
                    cur.next = temp
                if temp.left:
                    q.put(temp.left)
                    q.put(temp.right)
                cur = temp
    
        return root
