class Solution:
    def alphabetBoardPath(self, s: str) -> str:
        dic = {}
        c = 97
        for i in range(5):
            for j in range(5):
                dic[chr(c)] = [i, j]
                c += 1
        
        dic[chr(c)] = [5, 0]

        jvrc = ''
        x, y = 0, 0

        for i in range(len(s)):
            a = dic[s[i]][0]
            b = dic[s[i]][1]
            
            if x == 5 and y == 0:
                if x-a <= 0:
                    jvrc += ((abs(x-a) * 'D'))
                else:
                    jvrc += (abs(x-a) * 'U')
                
                if y-b <= 0:
                    jvrc += (abs(y-b) * 'R')
                else:
                    jvrc += (abs(y-b) * 'L')
                
            else:
                if y-b <= 0:
                    jvrc += (abs(y-b) * 'R')
                else:
                    jvrc += (abs(y-b) * 'L')
                if x-a <= 0:
                    jvrc += ((abs(x-a) * 'D'))
                else:
                    jvrc += (abs(x-a) * 'U')
            
            jvrc += '!'

            x, y = a, b
        
        return jvrc


        