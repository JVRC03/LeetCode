class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [1, i]
            else:
                dic[s[i]][0] += 1
        
        for i in dic:
            if dic[i][0] == 1:
                return dic[i][1]
        
        return -1

        