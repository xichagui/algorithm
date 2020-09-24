# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        max_count = 0
        count = 0
        temp = None
        
        def update(node):
            nonlocal count
            nonlocal max_count
            nonlocal ans
            
            if count == max_count:
                ans.append(node.val)
            elif count > max_count:
                max_count = count
                ans = [node.val]
        
        def ldr(node):
            nonlocal temp
            nonlocal count
            
            if not node:
                return
            
            ldr(node.left)
            
            if node.val == temp:
                count += 1
                update(node)
            else:
                temp = node.val
                count = 1
                update(node)
            
            ldr(node.right)
        
        ldr(root)
        return ans
