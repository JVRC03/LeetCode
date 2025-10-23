class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            jvrc = ''
            for i in range(len(s)-1):
                k = (int(s[i]) + int(s[i+1]))%10
                jvrc += str(k)
            s = jvrc
        
        if len(s) == 2 and s[0] == s[1]:
            return True
        
        return False

        