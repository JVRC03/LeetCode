class Solution:
    def percentageLetter(self, s: str, k: str) -> int:
        jvrc = 0

        for i in range(len(s)):
            if s[i] == k:
                jvrc += 1
        
        return int(jvrc / len(s) * 100)

        