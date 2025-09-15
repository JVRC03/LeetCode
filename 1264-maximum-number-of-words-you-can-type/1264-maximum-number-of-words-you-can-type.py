class Solution:
    def canBeTypedWords(self, s: str, a: str) -> int:
        v = set(list(a))
        jvrc = 0

        i = 0
        while i < len(s):
            c = 0
            while i < len(s) and s[i] != ' ':
                if s[i] in v:
                    while i < len(s) and s[i] != ' ':
                        i += 1
                    c = 1
                    break
                i += 1
                
            if not c:
                jvrc += 1
            i += 1
            
        return jvrc
        