class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one(num):
            count = 0
            while num:
                num &= num - 1
                count += 1
            return count
        
        # bin(1) -> 0b1
        # return sorted(arr, key=lambda x: (bin(x).coung('1'), x))
        return sorted(arr, key=lambda x: (count_one(x), x))

