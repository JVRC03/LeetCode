class Solution:
    def maximumLength(self, s: str) -> int:
        jvrc = -1
        def f(k):
            c = 0
            
            if s[0:len(k)] == k:
                c += 1
    
            for i in range(len(k), len(s)):
                if s[i-len(k)+1:len(k)+(i-len(k)+1)] == k:
                    c += 1
                if c >= 3:
                    return 1
            
            return 0

        for i in range(len(s)):
            temp = ''
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    break
                temp += s[j]
                if f(temp):
                    jvrc = max(jvrc, len(temp))

        return jvrc
                    
        