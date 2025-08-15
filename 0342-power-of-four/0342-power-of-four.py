class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        if n == 1:
            return True
        
        s = bin(n)
        s = s[2:]

        if n >= 4 and s.count('1') == 1 and s.count('0')%2 == 0:
            return True
        
        return False
        