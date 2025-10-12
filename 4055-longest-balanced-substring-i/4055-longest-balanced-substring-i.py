class Solution:
    def longestBalanced(self, s: str) -> int:
        jvrc = 0

        def check(dic):
            curr = 0
            tot = 0
            for i in dic:
                if curr == 0:
                    curr = dic[i]
                tot += dic[i]
                
            for i in dic:
                if dic[i] != curr:
                    return False, tot
            
            return True, tot

        for i in range(len(s)):
            dic = {}
            for j in range(i, len(s)):
                if s[j] not in dic:
                    dic[s[j]] = 1
                else:
                    dic[s[j]] += 1
                
                a, b = check(dic)
                if a:
                    jvrc = max(jvrc, b)
        
        return jvrc
        