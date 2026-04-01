class Solution:


    def isThree(self, n: int) -> bool:

        c = 0
        for i in range(1, n+1):
            if n%i == 0:
                c += 1
            
            if c > 3:
                return False
        
        if c == 3:
            return True
        
        return False
        