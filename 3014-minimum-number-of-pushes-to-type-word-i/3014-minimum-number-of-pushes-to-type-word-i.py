class Solution:
    def minimumPushes(self, s: str) -> int:
        jvrc = 0
        dic = {}
        c = 0

        for i in range(len(s)):
            if s[i] in dic:
                jvrc += c
            else:
                if len(dic) % 8 == 0:
                    c += 1
                dic[s[i]] = c
                jvrc += c
        
        return jvrc