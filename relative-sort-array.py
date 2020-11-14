class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        value_dict = {val: index for index, val in enumerate(arr2)}
        
        def get_value(val):
            if val in value_dict:
                return value_dict[val]
            else:
                return val + 1000
        
        return sorted(arr1, key=get_value)

