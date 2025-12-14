class Solution:
    def reverseWords(self, s: str) -> str:

        def get():
            c = 0
            idx = -1
            t = ''

            for i in range(len(s)):
                t += s[i]
                if s[i] == ' ':
                    idx = i+1
                    break
                
                if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                    c += 1
            
            if idx == -1:
                idx = len(s)
            
            return c, idx, t

        k, st, jvrc = get()

        t, c = '', 0

        for i in range(st, len(s)):
            if s[i] != ' ':
                t += s[i]
                if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                    c += 1
                continue
            
            if c == k:
                t = t[::-1]
            
            jvrc += t
            jvrc += ' '
            c, t = 0, ''
        
        if c == k:
            t = t[::-1]
        
        jvrc += t
        
        return jvrc

                     

        