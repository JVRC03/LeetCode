class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
            
        jvrc = 0
        c = 0

        for i in dic:
            if dic[i]%2 == 0:
                jvrc += dic[i]
            else:
                k = dic[i]-1
                jvrc += k

                c = 1
                                
        if c:
            return jvrc+1

        return jvrc

