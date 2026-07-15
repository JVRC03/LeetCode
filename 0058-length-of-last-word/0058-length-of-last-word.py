class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        jvrc, sp = 0, 0

        for i in range(len(s)-1, -1, -1):
            if jvrc and s[i] == ' ':
                break
            
            if s[i] == ' ':
                sp = 1
            else:
                jvrc += 1

        return jvrc
        