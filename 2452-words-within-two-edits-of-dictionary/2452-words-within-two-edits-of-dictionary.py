class Solution:
    def twoEditWords(self, a: List[str], b: List[str]) -> List[str]:
        dic = {}
        jvrc = []

        for i in range(len(b)):
            dic[b[i]] = 1
        
        for i in range(len(a)):
            for j in dic:
                if len(j) == len(a[i]):
                    c = 0
                    for k in range(len(j)):
                        if j[k] != a[i][k]:
                            c += 1
                    if c < 3:
                        jvrc.append(a[i])
                        break
            
        return jvrc



            

        