class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even = 0, 0
        o, e = 1, 2

        for i in range(n):
            odd += o
            even += e

            o += 2
            e += 2
        
        def gcd(a, b):
            if b == 0:
                return a
            
            if a > b:
                return gcd(b, a % b)
            
            return gcd(a, b % a)
        
        return gcd(min(even, odd), max(even, odd))
        