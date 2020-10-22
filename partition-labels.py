class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {s: i for i, s in enumerate(S)}
        res = []
        end = 0
        mark = -1
        for i, s in enumerate(S):
            end = max(end, d[s])
            if i == end:
                res.append(i - mark)
                mark = i
        return res
