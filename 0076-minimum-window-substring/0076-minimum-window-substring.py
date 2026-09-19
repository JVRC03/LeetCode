class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic, main = [0] * 130, [0] * 130

        for i in range(len(t)):
            main[ord(t[i])] += 1
        
        def check():
            for i in range(130):
                if main[i] > dic[i]:
                    return False
            return True 

        jvrc = ''
        f, r = 0, 0
        while f <= r and r < len(s):
            dic[ord(s[r])] += 1
            
            while check():
                if len(jvrc) == 0:
                    jvrc = s[f:r + 1]
                else:
                    temp = s[f:r + 1]
                    if len(temp) < len(jvrc):
                        jvrc = temp
                    elif len(temp) == len(jvrc):
                        jvrc = min(jvrc, temp)
                
                dic[ord(s[f])] -= 1
                f += 1

            r += 1

        return jvrc
            

        