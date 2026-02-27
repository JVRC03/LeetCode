class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        vis = [0] * 26

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
            
            vis[ord(s[i])%97] = i
        
        for i in dic:
            if dic[i] == 1:
                return vis[ord(i)%97]
        
        return -1
        
        