# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val=val)
        
        node = root
        while True:
            if node.val <= val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val=val)
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val=val)
                    break
        
        return root
