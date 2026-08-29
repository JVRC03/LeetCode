class Solution:
    def numberOfMatches(self, n: int) -> int:
        jvrc = 0

        while n > 1:
            jvrc += n // 2

            if n % 2 == 0:
                n //= 2
                continue
            
            n //= 2
            n += 1
        
        return jvrc

        