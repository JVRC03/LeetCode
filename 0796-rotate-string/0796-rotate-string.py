class Solution:
    def rotateString(self, s: str, k: str) -> bool:
        curr = ''

        if s == k:
            return True

        for i in range(len(s)):
            curr += s[i]
            temp = s[i+1:]
            kk = temp + curr

            if kk == k:
                return True
        
        return False
        