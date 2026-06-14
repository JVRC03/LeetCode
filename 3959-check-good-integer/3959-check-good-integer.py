class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        sq, curr = 0, 0
        while n:
            rem = n % 10
            sq += (rem * rem)
            curr += rem

            n //= 10
        
        if sq-curr >= 50:
            return True
        
        return False
        