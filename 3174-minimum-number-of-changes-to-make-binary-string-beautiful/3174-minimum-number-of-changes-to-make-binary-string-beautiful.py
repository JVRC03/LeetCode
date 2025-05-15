class Solution:
    def minChanges(self, s: str) -> int:
        o, z = 0, 0
        jvrc = 0
        for i in range(len(s)):
            if s[i] == '0':
                if o%2 == 0:
                    o = 0
                    z += 1
                else:
                    jvrc += 1
                    o = 0    
            else:
                if z%2 == 0:
                    z = 0
                    o += 1
                else:
                    z = 0
                    jvrc += 1
        
        return jvrc
        