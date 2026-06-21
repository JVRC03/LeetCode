class Solution:
    def maxDistance(self, s: str) -> int:
        l, r, d, u, e = 0, 0, 0, 0, 0

        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            elif s[i] == 'R':
                r += 1
            elif s[i] == 'D':
                d += 1
            elif s[i] == 'U':
                u += 1
            else:
                e += 1
        
        jvrc = abs(l - r) + abs(u - d)

        return jvrc + e
        
        
        