class Solution:
    def maxDepth(self, s: str) -> int:
        jvrc, curr = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                curr += 1
            elif s[i] == ')':
                curr -= 1
            
            jvrc = max(jvrc, curr)

        return jvrc
        