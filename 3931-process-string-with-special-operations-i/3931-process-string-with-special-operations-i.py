class Solution:
    def processStr(self, s: str) -> str:
        jvrc = []

        for i in range(len(s)):
            if s[i].isalpha():
                jvrc.append(s[i])
            elif s[i] == '*':
                if len(jvrc):
                    jvrc.pop()
            elif s[i] == '#':
                jvrc.extend(jvrc)
            else:
                jvrc = jvrc[::-1]
        
        return ''.join(jvrc)
        