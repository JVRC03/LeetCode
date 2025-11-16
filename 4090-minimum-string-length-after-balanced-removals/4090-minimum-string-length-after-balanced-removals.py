class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a, b = 0, 0

        for i in range(len(s)):
            if s[i] == 'a':
                a += 1
            else:
                b += 1
            
            if a and b:
                a -= 1
                b -= 1
        
        return (a + b)