class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        jvrc = 0
        c = 0
        count = 1

        for i in range(len(s)):
            count = 1
            c = 0
            for j in range(i, len(s)-1):
                if s[j] != s[j+1]:
                    count += 1
                else:
                    if not c:
                        c = 1
                        count += 1
                    else:
                        jvrc = max(jvrc, count)
                        c = 0
                        break
        
            
            jvrc = max(jvrc, count)
        
        jvrc = max(jvrc, count)

        return jvrc
    
