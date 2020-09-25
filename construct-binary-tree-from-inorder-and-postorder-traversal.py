# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         if not inorder:
#             return None
        
#         mid = postorder[-1]
#         root = TreeNode(mid)
        
#         if len(inorder) == 1:
#             return root
        
#         for index, num in enumerate(inorder):
#             if num == mid:
#                 root.left = self.buildTree(inorder[0:index], postorder[0:index])
#                 root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
#         return root
        
        def inner(left, right):
            if left > right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            index =  inorder_dict[root_val]
            
            root.right = inner(index + 1, right)
            root.left = inner(left, index - 1)
            
            return root
        
        inorder_dict = {num: index for index, num in enumerate(inorder)}
        
        return inner(0, len(inorder) - 1)
