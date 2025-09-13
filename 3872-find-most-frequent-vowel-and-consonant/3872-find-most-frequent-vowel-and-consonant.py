class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic = {}
        v = {'a', 'e', 'i', 'o', 'u'}
        jv, rc = 0, 0

        for i in range(len(s)):
            if s[i] in v:
                if s[i] not in dic:
                    dic[s[i]] = 1
                else:
                    dic[s[i]] += 1
                
                jv = max(jv, dic[s[i]])
            else:
                if s[i] not in dic:
                    dic[s[i]] = 1
                else:
                    dic[s[i]] += 1
                
                rc = max(rc, dic[s[i]])
        
        return jv+rc
        
        