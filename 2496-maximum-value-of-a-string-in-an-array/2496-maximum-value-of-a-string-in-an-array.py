class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        jvrc = 0

        for i in range(len(strs)):
            stop = 0
            for j in range(len(strs[i])):
                if strs[i][j].isalpha():
                    stop = 1
                    break
            
            if stop:
                jvrc = max(jvrc, len(strs[i]))
            else:
                jvrc = max(jvrc, int(strs[i]))

        return jvrc        