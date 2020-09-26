# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans_list = []
        ans = []
        temp_sum = 0
        def inner(root, temp_sum, sum, ans):
            if root:
                ans.append(root.val)
                inner(root.left, temp_sum + root.val, sum, ans)
                inner(root.right, temp_sum + root.val, sum, ans)
                if root.left is None and root.right is None and temp_sum + root.val == sum:
                    ans_list.append(ans[::])
                ans.pop()
                    
        inner(root, 0, sum, ans)
        return ans_list
