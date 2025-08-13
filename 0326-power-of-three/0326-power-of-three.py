class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        c = 0

        while True:
            k = int(math.pow(3, c))
            if k == n:
                return True
            
            if k > n:
                return False
            
            c += 1
        
        return False
            
        