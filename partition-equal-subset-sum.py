class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        sum_of_lists = sum(nums)
        nums.sort()
        
        half_sum = sum_of_lists // 2
        max_num = nums[-1]
        if half_sum * 2 != sum_of_lists:
            return False
        
        if max_num > half_sum:
            return False
        
        dp = [False for _ in range(half_sum + 1)]
                
        dp[0] = True
        dp[nums[0]] = True
        
        for i in range(1, n):
            num = nums[i]
            for j in range(half_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[half_sum]
