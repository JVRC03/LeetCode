class Solution:
    def toLowerCase(self, s: str) -> str:
        jvrc = ''

        for i in range(len(s)):
            jvrc += s[i].lower()
        
        return jvrc
        