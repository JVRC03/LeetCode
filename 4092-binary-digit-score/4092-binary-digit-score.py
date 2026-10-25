class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1, s2 = 0, 0

        while a:
            s1 += (a % 2)
            a //= 2
        
        while b:
            s2 += (b % 2)
            b //= 2
        
        if s1 >= s2:
            return s1 * s2
        
        return s2 // s1
        