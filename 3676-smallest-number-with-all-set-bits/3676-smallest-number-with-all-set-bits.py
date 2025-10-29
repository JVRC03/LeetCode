class Solution:
    def smallestNumber(self, n: int) -> int:
        jvrc = ''

        while n:
            jvrc += '1'
            n //= 2
        
        return int(jvrc, 2)

        