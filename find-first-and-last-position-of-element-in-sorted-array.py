class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        
        def binary_serach(left, right, target, res):
            if left >= right:
                return
            
            mid = (left + right) // 2
            if nums[mid] == target:
                if res[0] == -1:
                    res[0] = res[1] = mid
                else:
                    res[0] = min(res[0], mid)
                    res[1] = max(res[1], mid)
                    
            if nums[mid] > target:
                binary_serach(left, mid, target, res)
            elif nums[mid] < target:
                binary_serach(mid + 1 , right, target, res)
            else:
                binary_serach(left, mid, target, res)
                binary_serach(mid + 1, right, target, res)
            
        if nums:
            binary_serach(0, len(nums), target, res)
        return res

