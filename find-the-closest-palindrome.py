class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num_n = int(n)
        len_n = len(n)
        flag = len_n % 2
        mid = len_n // 2
        
        if num_n <= 10:
            return str(num_n - 1)
        
        left = n[0: mid + flag]
        left_num = int(left)
        
        temp_bigger = str(num_n + 10 ** mid)
        
        num_temp_smaller = num_n
        for _ in range(mid):
            num_temp_smaller = num_temp_smaller // 10
        
        for _ in range(mid):
            num_temp_smaller *= 10
            
        num_temp_smaller -= 1
        temp_smaller = str(num_temp_smaller)
        
        palindrome = self.get_palindromic(n)
        bigger_palindrome = self.get_palindromic(temp_bigger)
        smaller_palindrome = self.get_palindromic(temp_smaller)
        
        num_temp = int(palindrome)
        num_bigger = int(bigger_palindrome)
        num_smaller = int(smaller_palindrome)
        
        abs_temp = abs(num_temp - num_n)
        abs_temp_bigger = abs(num_bigger - num_n)
        abs_temp_smaller = abs(num_smaller - num_n)
        
        abs_min = min(abs_temp, abs_temp_bigger, abs_temp_smaller) if abs_temp != 0 else min(abs_temp_bigger, abs_temp_smaller)
        print(palindrome, bigger_palindrome,smaller_palindrome)
        
        if abs_min == abs_temp_smaller:
            return smaller_palindrome
        elif abs_min == abs_temp:
            return palindrome
        else:
            return bigger_palindrome 
        
    def get_palindromic(self, n):
        num_n = int(n)
        len_n = len(n)
        flag = len_n % 2
        mid = len_n // 2
        
        if num_n < 10:
            return str(num_n)
        
        left = n[0: mid]
        return left + n[mid: mid + flag] + left[::-1]
                
