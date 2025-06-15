class Solution:
    def generateTag(self, s: str) -> str:
        jvrc = '#'
        f = 0

        while f < len(s):
            if s[f] == ' ':
                while f < len(s) and s[f] == ' ':
                    f += 1
                if f < len(s) and s[f].isalpha():
                    if jvrc[-1] == '#':
                        jvrc += s[f].lower()
                    else:
                        jvrc += s[f].upper()

            elif s[f].isalpha():
                if jvrc[-1] == '#':
                    jvrc += s[f].lower()
                    f += 1
                    continue
                jvrc += s[f].lower()
            
            if len(jvrc) == 100:
                break
            
            f += 1
        
        return jvrc

        

        