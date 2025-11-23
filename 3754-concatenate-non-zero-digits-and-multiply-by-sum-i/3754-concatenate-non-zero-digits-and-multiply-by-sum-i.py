class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        jvrc = ''
        n = 0

        for i in range(len(s)):
            if s[i] != '0':
                jvrc += s[i]
                n += int(s[i])
        
        if not len(jvrc):
            jvrc = 0
            
        return int(jvrc) * n
        