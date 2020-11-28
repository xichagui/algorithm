class Solution:
    def reversePairs(self, nums: List[int]) -> int:
            
        def reverse_pairs_recursive(nums, left, right):
            if right - left < 2:
                return 0
            
            mid = (right - left) // 2 + left
            res_left = reverse_pairs_recursive(nums, left, mid)
            res_right = reverse_pairs_recursive(nums, mid, right)
            
            i, j = left, mid
            temp = 0
            while i < mid and j < right:
                if nums[i] > nums[j] * 2:
                    temp += right - j
                    i += 1
                else:
                    j += 1
            
            i, j = left, mid
            temp_list = []
            while i < mid and j < right:
                if nums[i] > nums[j]:
                    temp_list.append(nums[i])
                    i += 1
                else:
                    temp_list.append(nums[j])
                    j += 1
            
            while i < mid:
                temp_list.append(nums[i])
                i += 1
            
            while j < right:
                temp_list.append(nums[j])
                j += 1
            
            for i in range(len(temp_list)):
                nums[left + i] = temp_list[i]
            
            return res_left + res_right + temp
        
        if len(nums) < 2:
            return 0
        
        return reverse_pairs_recursive(nums, 0, len(nums))
        
