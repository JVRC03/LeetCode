class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        f, r = 0, len(s)-1

        while f <= r:
            if s[f] == s[r]:
                return f
            
            f += 1
            r -= 1
        
        return -1
        