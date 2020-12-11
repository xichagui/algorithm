from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.popleft() + n)
                dire.popleft()
            else:
                dire.append(dire.popleft() + n)
                radiant.popleft()
        
        return 'Radiant' if radiant else 'Dire'

