# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        per = None
        while len(stack) > 0 or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1]
                if cur.right is None or cur.right == per:
                    res.append(cur.val)
                    stack.pop()
                    per = cur
                    cur = None
                else:
                    cur = cur.right
        
        return res
