class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        if nums[0] == 0:
            return False

        for i in range(1, n - 1):
            nums[i] = nums[i] if nums[i] > nums[i - 1] - 1 else nums[i - 1] - 1
            
            if nums[i] == 0:
                return False
        
        return True
