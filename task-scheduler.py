class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = len(tasks)
        if n == 0:
            return size
        
        counter = collections.Counter(tasks)
        _max = 0
        _max_kind = 0
        for c in counter:
            if (temp_counter := counter[c]) > _max:
                _max = temp_counter
                _max_kind = 0
            if temp_counter == _max:
                _max_kind += 1
        return max((_max - 1) * (n + 1) + _max_kind, size)

