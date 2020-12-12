class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (res := len(nums)) < 2:
            return res
        else:
            res = 1
        
        cur = nums[0]
        flag = None
        
        for num in nums[1:]:
            if num == cur:
                continue
            
            if flag is None:
                flag = (num - cur) > 0
                res += 1
            else:
                if flag != ((num - cur) > 0):
                    res += 1
                    flag = (num - cur) > 0
            
            cur = num
        
        return res
    
