class Solution:
    def isValid(self, s: str) -> bool:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if len(s) < 3:
            return False
        
        vo, co = 0, 0

        for i in range(len(s)):
            if s[i].isdigit():
                continue
            
            if s[i] in v:
                vo = 1
            elif s[i].isalpha():
                co = 1
            else:
                return False
        
        if not vo or not co:
            return False
        
        return True
        