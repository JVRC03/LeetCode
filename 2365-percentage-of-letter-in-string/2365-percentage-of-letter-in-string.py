class Solution:
    def percentageLetter(self, s: str, k: str) -> int:
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        if k in dic:
            return int((dic[k]/len(s)) * 100)
        
        return 0
        