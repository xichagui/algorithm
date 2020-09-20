class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums:
            return res
        
        # res.append(nums)
        size = len(nums)
        temp = []
        self.dfs(nums, 0, size, temp, res)
        
        return res
        
    def dfs(self, nums, index, size, temp, res):
        for i in range(index, size):
            temp.append(nums[i])
            res.append(temp.copy())
            self.dfs(nums, i + 1, size, temp, res)
            temp.pop()
