class Solution:
    def removeZeros(self, n: int) -> int:
        jvrc = ''
        s = str(n)

        for i in range(len(s)):
            if s[i] != '0':
                jvrc += s[i]

        return int(jvrc)
        