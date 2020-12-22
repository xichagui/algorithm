# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        reverse = True
        dp = collections.deque()
        dp.append(root)
        
        while size := len(dp):
            temp = []
            for _ in range(size):
                node = dp.popleft()
                if not reverse:
                    temp.insert(0, node.val)
                else:
                    temp.append(node.val)
                
                if node.left:
                    dp.append(node.left)
                if node.right:
                    dp.append(node.right)
            
            res.append(temp)
            reverse = not reverse
        
        return res

