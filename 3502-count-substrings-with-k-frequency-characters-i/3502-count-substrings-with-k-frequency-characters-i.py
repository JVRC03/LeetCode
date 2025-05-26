class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        jvrc = 0

        for i in range(len(s)):
            dic = {}
            for j in range(i, len(s)):
                if s[j] not in dic:
                    dic[s[j]] = 1
                else:
                    dic[s[j]] += 1
                if dic[s[j]] >= k:
                    jvrc += (len(s)-j)
                    break
        
        return jvrc


        