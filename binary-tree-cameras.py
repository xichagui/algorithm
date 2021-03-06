# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return [float("inf"), 0, 0]
            
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            
            a = lc + rc + 1
            b = min(a, la + rb, lb + ra)
            c = min(a, lb + rb)
            return [a, b, c]
        
        a, b, c = dfs(root)
        return b
