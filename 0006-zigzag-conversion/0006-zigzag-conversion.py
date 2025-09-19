class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        dic = {}
        for i in range(n):
            dic[i] = ''
        jvrc = ''

        i = 0
        c = 0

        while i < len(s):
            if c%2 == 0:
                if i == 0:
                    for ie in range(n):
                        if i < len(s):
                            dic[ie] += s[i]
                            i += 1
                else:
                    for ie in range(1, n):
                        if i < len(s):
                            dic[ie] += s[i]
                            i += 1
            else:
                for ie in range(n-2, -1, -1):
                    if i < len(s):
                        dic[ie] += s[i]
                        i += 1
    
            c += 1
        
        for i in dic:
            jvrc += dic[i]
        
        return jvrc


            


        