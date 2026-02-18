class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1

        while n:
            k = n%2

            if k != prev:
                prev = k
                n //= 2
                continue
            
            return False
        
        return True
        