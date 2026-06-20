class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        jvrc = ''
        curr = 0

        for i in range(len(s)):
            if s[i] == ' ':
                curr += 1
            
            if curr == k:
                break
            
            jvrc += s[i]
        
        return jvrc
        