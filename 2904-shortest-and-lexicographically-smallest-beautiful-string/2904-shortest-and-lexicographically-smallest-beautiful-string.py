class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        f, r = 0, 0
        jvrc = ''

        while f <= r and r < len(s):
            if s[r] == '1':
                k -= 1
            
            if k == 0:
                while s[f] == '0':
                    f += 1
                temp = s[f:r + 1]
                if len(jvrc) == 0:
                    jvrc = temp
                else:
                    if len(jvrc) > len(temp):
                        jvrc = temp
                    elif len(jvrc) == len(temp):
                        jvrc = min(jvrc, temp)

            if k == -1:
                while s[f] == '0':
                    f += 1
                
                f += 1
                while s[f] == '0':
                    f += 1

                temp = s[f:r + 1]
                if len(jvrc) == 0:
                    jvrc = temp
                else:
                    if len(jvrc) > len(temp):
                        jvrc = temp
                    elif len(jvrc) == len(temp):
                        jvrc = min(jvrc, temp)
                k = 0
            
            r += 1
        
        return jvrc

            


        