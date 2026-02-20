class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)
        s = s[2:]

        jvrc = 0
        a = -1

        for i in range(len(s)):
            if s[i] == '1':
                if a == -1:
                    a = i
                else:
                    jvrc = max(jvrc, i-a)
                    a = i
            
        return jvrc
                

        

        