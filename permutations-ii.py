class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l == 0:
            return []
        
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()
                
        nums.sort()
        
        used = [False] * l
        res = []
        
        dfs(nums, l, 0, [], used, res)
        return res
