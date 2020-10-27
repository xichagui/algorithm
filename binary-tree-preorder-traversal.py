# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 非递归
        res = []
        if not root:
            return res
        
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        
        return res


# 递归    
#         if not root:
#             return []
        
#         res = []
        
#         def fun(node: TreeNode, res: List):
#             res.append(node.val)
#             if node.left:
#                 fun(node.left, res)
#             if node.right:
#                 fun(node.right, res)
        
#         fun(root, res)
        
#         return res

