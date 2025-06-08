class Solution:
    def maxSubstrings(self, s: str) -> int:
        dic = {}
        jvrc = 0

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                if i-dic[s[i]]+1 >= 4:
                    jvrc += 1
                    dic = {}
        
        return jvrc

