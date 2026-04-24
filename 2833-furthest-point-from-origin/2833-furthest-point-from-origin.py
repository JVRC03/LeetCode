class Solution:
    def furthestDistanceFromOrigin(self, s: str) -> int:
        l, r, d = 0, 0, 0

        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            elif s[i] == 'R':
                r += 1
            else:
                d += 1
        
        return max(l, r) + d - min(l, r)
        