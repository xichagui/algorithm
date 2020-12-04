import collections


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count_map = collections.Counter(nums)
        end_map = collections.Counter()
        
        for x in nums:
            if (count := count_map[x]) > 0:
                if end_map[x - 1] > 0:
                    count_map[x] -= 1
                    end_map[x - 1] -= 1
                    end_map[x] += 1
                else:
                    if count_map[x + 1] > 0 and count_map[x + 2] > 0:
                        count_map[x] -= 1
                        count_map[x + 1] -= 1
                        count_map[x + 2] -= 1
                        end_map[x + 2] += 1
                    else:
                        return False
                    
        return True

