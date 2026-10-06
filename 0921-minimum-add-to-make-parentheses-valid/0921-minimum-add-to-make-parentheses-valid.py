class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        jvrc, left = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                if left:
                    left -= 1
                    continue
                
                jvrc += 1
        
        jvrc += left
        
        return jvrc
        
        