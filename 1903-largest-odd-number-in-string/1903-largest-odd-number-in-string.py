class Solution:
    def largestOddNumber(self, s: str) -> str:
        idx = -1

        for i in range(len(s)-1, -1, -1):
            if int(s[i])%2 == 1:
                idx = i
                break
        
        if idx == -1:
            return ''
        
        return s[0:i+1]
        