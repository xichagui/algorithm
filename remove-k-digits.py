class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        res_list = []
        
        if len(num) == k:
            return '0'
        
        i = 0
        while i < len(num):
            if len(res_list) == 0:
                res_list.append(num[i])
                i += 1
            else:
                if res_list[-1] > num[i] and k > 0:
                    res_list.pop()
                    k -= 1
                else:
                    res_list.append(num[i])
                    i += 1
        
        if k:
            res_list = res_list[:-k]
        
        return ''.join(res_list).lstrip('0') or '0'
        
