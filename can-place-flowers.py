class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
        i = 1
        while n > 0 and i < len(flowerbed) - 1:
            if flowerbed[i] == 0:
                if flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                    n -= 1
                    flowerbed[i] = 1
            i += 1
        
        return True if n == 0 else False

