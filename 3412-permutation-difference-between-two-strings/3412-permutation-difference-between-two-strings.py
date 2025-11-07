class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        
        jvrc = 0

        for i in range(len(t)):
            jvrc += abs(dic[t[i]]-i)
        
        return jvrc
        