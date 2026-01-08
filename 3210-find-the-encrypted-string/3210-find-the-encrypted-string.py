class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        jvrc = ''

        for i in range(len(s)):
            if i+k < len(s):
                jvrc += s[i+k]
                continue
            
            jvrc += s[(i+k)%len(s)]
        
        return jvrc
        