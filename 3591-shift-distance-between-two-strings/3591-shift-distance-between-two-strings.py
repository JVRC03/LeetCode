class Solution:
    def shiftDistance(self, s: str, t: str, n: List[int], p: List[int]) -> int:
        jvrc = 0

        for i in range(len(s)):
            a, b = 0, 0
            x = ord(s[i])%97
            y = ord(t[i])%97

            for j in range(26):
                if (x)%26 == y:
                    break
                a += n[(x)%26]
                x += 1
                if x == 26:
                    x = 0
            x = ord(s[i])%97
            for j in range(26):
                if (x)%26 == y:
                    break
                b += p[(x)%26]
                x -= 1
                if x == -1:
                    x = 25
                
            jvrc += min(a, b)
            
        return jvrc        