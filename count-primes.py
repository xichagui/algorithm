class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        primes = []
        int_list = [1] * n
        count = 0
        for i in range(2, n):
            if int_list[i]:
                primes.append(i)
                count += 1
                
            j = 0
            while j < count and primes[j] * i < n:
                int_list[i * primes[j]] = 0
                if i % primes[j] == 0:
                    break
                j += 1

        return count
                
