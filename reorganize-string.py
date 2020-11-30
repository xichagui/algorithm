class Solution:
    def reorganizeString(self, S: str) -> str:
        
        l = len(S)
        count_list = [0] * 26
        for s in S:
            count_list[ord(s) - 97] += 1
        
        max_count = 0
        max_index = -1
        for index, count in enumerate(count_list):
            if count > (l + 1) //2:
                return ""
            if count > max_count:
                max_count = count
                max_index = index
                
        res = [chr(max_index + 97)] * l
        count_list[max_index] = 0
        
        i = 1
        
        for index, count in enumerate(count_list):
            while count:
                if i >= l:
                    i = 0
                res[i] = chr(index + 97)
                i += 2
                count -= 1
        
        return ''.join(res)

