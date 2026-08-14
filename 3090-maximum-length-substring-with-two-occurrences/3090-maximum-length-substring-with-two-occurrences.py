class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        jvrc = 0
        dic = {}
        f, r = 0, 0

        while f <= r and r < len(s):
            if s[r] not in dic:
                dic[s[r]] = 1
            else:
                dic[s[r]] += 1
            
            if dic[s[r]] < 3:
                jvrc = max(jvrc, r - f + 1)
            else:
                while dic[s[r]] > 2:
                    dic[s[f]] -= 1
                    if not dic[s[f]]:
                        del dic[s[f]]
                    f += 1
            
            r += 1
        
        return jvrc

        