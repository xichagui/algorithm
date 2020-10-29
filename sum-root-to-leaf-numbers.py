# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        
        q = queue.Queue()
        val_q = queue.Queue()
        
        q.put(root)
        val_q.put(root.val)
        
        while not q.empty():
            node = q.get()
            val = val_q.get()
            
            if node.left:
                q.put(node.left)
                val_q.put(val * 10 + node.left.val)
                
            if node.right:
                q.put(node.right)
                val_q.put(val * 10 + node.right.val)
            
            if not node.left and not node.right:
                res += val
                
        return res
            
