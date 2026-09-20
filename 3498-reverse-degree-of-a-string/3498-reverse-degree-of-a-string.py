class Solution:
    def reverseDegree(self, s: str) -> int:
        jvrc = 0

        for i in range(len(s)):
            val = 26 - (ord(s[i]) % 97)
            jvrc += ((i + 1) * val)
        
        return jvrc