class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        jvrc, c = 0, 0
        z = 1000
        while z:
            if abs(n - c) <= k and (c & n) == 0:
                jvrc += c
            
            c += 1
            z -= 1
        
        return jvrc