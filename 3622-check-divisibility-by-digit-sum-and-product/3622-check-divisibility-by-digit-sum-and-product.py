class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a, b = 0, 1
        real = n

        while n:
            rem = (n % 10)
            a += rem
            b *= rem

            n //= 10
        
        if real % (a + b) == 0:
            return True
        return False
        