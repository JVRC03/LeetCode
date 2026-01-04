class Solution:
    def largestEven(self, s: str) -> str:
        r = len(s)-1
        
        while r >= 0 and int(s[r])%2 == 1:
            r -= 1

        return s[:r+1]
        