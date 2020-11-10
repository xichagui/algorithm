class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        
        p, q = i + 1, len(nums) - 1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1

