class Solution:
    def maxDepth(self, s: str) -> int:
        count, jvrc = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                jvrc = max(jvrc, count)
            elif s[i] == ')':
                count -= 1
            else:
                continue
        
        return jvrc
        