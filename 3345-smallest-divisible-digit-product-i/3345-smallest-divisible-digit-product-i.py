class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s = str(n)
            c = 1

            for i in range(len(s)):
                c *= int(s[i])
            
            if c % t == 0:
                return n
            
            n += 1
        