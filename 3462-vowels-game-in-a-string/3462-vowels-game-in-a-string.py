class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(len(s)):
            if s[i] in v:
                return True
        
        return False
        