# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res
        
    
    def dfs(self, node):
        if node is None:
            return
        
        if node.left:
            if not (node.left.left or node.left.right):
                self.res += node.left.val
            else:
                self.dfs(node.left)
        
        if node.right:
            self.dfs(node.right)
