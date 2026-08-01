class Solution:
    def canMakePaliQueries(self, s: str, q: List[List[int]]) -> List[bool]:
        jvrc, temp = [], [0] * 26
        dic = {}

        for i in range(len(s)):
            temp[ord(s[i]) % 97] += 1
            dic[i] = temp.copy()
                
        for i in range(len(q)):
            a = []

            if q[i][0] == 0:
                a = dic[q[i][1]]
            else:
                idx = q[i][0] - 1
                for j in range(26):
                    val = dic[q[i][1]][j] - dic[idx][j]
                    a.append(val)
            
            odd = 0

            for j in range(len(a)):
                if a[j] % 2 == 1:
                    odd += 1
            
            if odd < 2:
                jvrc.append(True)
                continue
            
            if odd // 2 > q[i][-1]:
                jvrc.append(False)
            else:
                jvrc.append(True)
        
        return jvrc


            

        