class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        f, r = 0, int(math.sqrt(c))+1

        while f <= r:
            k = (f*f)+(r*r)
            if k == c:
                return True
            
            if k > c:
                r -= 1
            else:
                f += 1
        
        return False
        