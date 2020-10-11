# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l = []
        minimum_d = float('inf')
        def ldr(node):
            nonlocal minimum_d
            if node:
                ldr(node.left)
                if l:
                    temp = node.val - l[-1]
                    minimum_d = temp if temp < minimum_d else minimum_d
                l.append(node.val)
                ldr(node.right)
        ldr(root)
        
        return minimum_d
