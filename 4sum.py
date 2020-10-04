class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        l = len(nums)

        h = 0
        while h < l - 3:
            a = nums[h]
            i = h + 1
            while i < l - 2:
                b = nums[i]
                j = i + 1
                k = l - 1
                while j < k:
                    c = nums[j]
                    d = nums[k]
                    temp_4_sum = a + b + c + d
                    if temp_4_sum == target:
                        res.append([a, b, c, d])
                    elif temp_4_sum > target:
                        while nums[k] == d and k > j:
                            k -= 1
                        continue
                    elif temp_4_sum < target:
                        while nums[j] == c and j < k:
                            j += 1
                        continue
                    while nums[k] == d and j < k:
                        k -= 1
                    while nums[j] == c and j < k:
                        j += 1
                while nums[i] == b and i < l - 2:
                    i += 1
            while nums[h] == a and h < l - 3:
                h += 1

        return res
