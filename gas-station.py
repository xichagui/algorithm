class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = run = start = 0
        
        for i in range(len(gas)):
            run += (gas[i] - cost[i])
            rest += (gas[i] - cost[i])
            
            if run < 0:
                start = i + 1
                run = 0
        
        return start if rest >= 0 else -1

