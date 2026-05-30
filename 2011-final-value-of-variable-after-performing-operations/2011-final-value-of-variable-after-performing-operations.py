class Solution:
    def finalValueAfterOperations(self, s: List[str]) -> int:
        jvrc = 0

        for i in range(len(s)):
            if s[i][0] == '-' or s[i][-1] == '-':
                jvrc -= 1
            else:
                jvrc += 1
        
        return jvrc

        