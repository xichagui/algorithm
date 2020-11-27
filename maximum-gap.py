class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        
        min_num = min(nums)
        max_num = max(nums)
        
        d = max(1, (max_num - min_num) // (size - 1))
        
        bucket_size = (max_num - min_num) // d + 1
        
        bucket_min_list = [-1] * bucket_size
        bucket_max_list = [-1] * bucket_size
        
        for num in nums:
            i = 0
            temp = num
            i = (num - min_num) // d
            
            if bucket_min_list[i] == -1 or temp < bucket_min_list[i]:
                bucket_min_list[i] = temp
            
            if bucket_max_list[i] == -1 or temp > bucket_max_list[i]:
                bucket_max_list[i] = temp
            
        res = 0
        last_max = bucket_max_list[0]
        
        for i in range(1, bucket_size):
            if last_max != -1:
                if bucket_min_list[i] != -1:
                    res = max(bucket_min_list[i] - last_max, res)
                    
            if bucket_max_list[i] != -1:
                last_max = bucket_max_list[i]
        
        return res
