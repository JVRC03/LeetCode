class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b, c = 0, 1, 1
        tot = a + b + c
        
        while tot <= n:

            if tot == n:
                return True

            curr = tot
            a = b
            b = c
            c = a + b
            
            tot = a + b + c

        return False
        