class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        a, b, mid = -1, -1, 1000

        for i in range(len(s)):
            if s[i] == '1':
                if a == -1:
                    a = i
                    b = i
                else:
                    b = i
            else:
                if mid == 1000:
                    mid = i
        
        if a <= b <= mid:
            return True

        return False        