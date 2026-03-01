class Solution:
    def minPartitions(self, s: str) -> int:
        jvrc = -1

        for i in range(len(s)):
            jvrc = max(jvrc, int(s[i]))
        
        return jvrc
        