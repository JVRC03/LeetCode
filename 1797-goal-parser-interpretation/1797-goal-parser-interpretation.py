class Solution:
    def interpret(self, s: str) -> str:
        jvrc, i = '', 0   

        while i < len(s):
            if s[i] == 'G':
                jvrc += s[i]
                i += 1
                continue
            
            if s[i] == '(':
                if s[i+1] == ')':
                    jvrc += 'o'
                    i += 2
                    continue
                jvrc += 'al'
                i += 4
        
        return jvrc
            
            
        