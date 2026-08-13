class Solution:
    def reformat(self, s: str) -> str:
        dig, char = [], []

        for i in range(len(s)):
            if s[i].isalpha():
                char.append(s[i])
            else:
                dig.append(s[i])
        
        def func(a, b):
            jvrc = ''

            while len(a) and len(b):
                jvrc += a.pop()
                jvrc += b.pop()
        
            if len(a) == 1:
                jvrc += a.pop()
            
            if len(a) or len(b):
                return ''
            
            return jvrc

        if len(dig) > len(char):
            return func(dig, char)
        
        return func(char, dig)

        