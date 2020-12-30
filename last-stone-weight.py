class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            stone_a = heapq.heappop(heap)
            stone_b = heapq.heappop(heap)
            
            stone_c = stone_a - stone_b
            if stone_c:
                heapq.heappush(heap, stone_c)
        
        return -heap[0] if len(heap) else 0

