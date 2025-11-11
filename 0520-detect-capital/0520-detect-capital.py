class Solution:
    def detectCapitalUse(self, s: str) -> bool:
        jvrc = 0

        for i in range(len(s)):
            if s[i].isupper():
                jvrc += 1
        
        if jvrc == 0 or (jvrc == 1 and s[0].isupper()) or jvrc == len(s):
            return True
        
        return False
        

        