class Solution:
    def numSub(self, s: str) -> int:
        f, r = 0, 0
        jvrc = 0

        while f <= r and r < len(s):
            if s[r] == '1':
                r += 1
                continue
            
            n = r-f
            jvrc += ((n * (n+1))//2)
            f = r+1
            r += 1
        
        n = r-f
        jvrc += ((n * (n+1))//2)

        return jvrc%1000000007

        