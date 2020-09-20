# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        temp = root
        if root:
            self.ldr(temp, 0)
        return root
    
    def ldr(self, node, temp_sum):
        if node.right:
            temp_sum = self.ldr(node.right, temp_sum)
            
        node.val += temp_sum
        temp_sum = node.val
        
        if node.left:
            temp_sum = self.ldr(node.left, temp_sum)
        return temp_sum
