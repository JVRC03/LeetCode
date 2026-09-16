class Solution:
    def removeTrailingZeros(self, s: str) -> str:
        jvrc, c = '', 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                if c == 0:
                    continue
                jvrc += s[i]
            else:
                jvrc += s[i]
                c = 1
        
        return jvrc[::-1]

        