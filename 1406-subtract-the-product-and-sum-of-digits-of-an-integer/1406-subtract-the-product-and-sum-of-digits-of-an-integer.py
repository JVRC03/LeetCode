class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 1, 0
        
        while n:
            k = (n%10)
            a *= k
            b += k
            n //= 10
        
        return a-b
        