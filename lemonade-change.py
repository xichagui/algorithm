class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = count_10 = 0
        
        for b in bills:
            if b == 5:
                count_5 += 1
                
            elif b == 10:
                if count_5 < 1:
                    return False
                count_5 -= 1
                count_10 += 1
            else:
                if count_10 >= 1 and count_5 >= 1:
                    count_5 -= 1
                    count_10 -= 1
                elif count_5 >= 3:
                    count_5 -= 3
                else:
                    return False
        
        return True

