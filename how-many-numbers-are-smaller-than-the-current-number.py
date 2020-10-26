class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_nums = [0] * 101
        
        for num in nums:
            count_nums[num] += 1
        
        temp = 0
        for i in range(101):
            count_nums[i] += temp
            temp = count_nums[i]
        
        res = []
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(count_nums[num - 1])
        
        return res

