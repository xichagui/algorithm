class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        def _re(start, end, nums):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        nums.reverse()
        _re(0, k - 1, nums)
        _re(k, len(nums) - 1, nums)
        
