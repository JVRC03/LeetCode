class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        jvrc = 0
        for i in range(len(s)):
            k = s[i].split(' ')
            jvrc = max(jvrc, len(k))
        
        return jvrc
        