class Solution:
    def maxPower(self, s: str) -> int:
        jvrc, curr = 0, 0
        char = s[0]

        for i in range(len(s)):
            if s[i] == char:
                curr += 1
            else:
                char = s[i]
                curr = 1

            jvrc = max(jvrc, curr)
        
        return jvrc

        