class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        f, r = 0, 0

        while f < len(s) and r < len(t):
            if s[f] == t[r]:
                f += 1    
            r += 1
        
        if f >= len(s):
            return True
        
        return False
        
        