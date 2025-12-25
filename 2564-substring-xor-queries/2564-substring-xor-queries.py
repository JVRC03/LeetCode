class Solution:
    def substringXorQueries(self, s: str, jvrc: List[List[int]]):
        dic = {}

        for i in range(len(s)):
            temp = ''
            for j in range(31):
                if i+j < len(s):
                    temp += s[i+j]
                    k = int(temp, 2)

                    if k not in dic:
                        dic[k] = [i, i+j]
                    else:
                        diff = dic[k][-1]+1-dic[k][0]
                        if diff > ((i+j-i)+1):
                            dic[k] = [i, i+j]
                    continue
                
                break
        
        for i in range(len(jvrc)):
            k = jvrc[i][0] ^ jvrc[i][-1]

            if k not in dic:
                jvrc[i] = [-1, -1]
                continue
            jvrc[i] = dic[k]
        
        return jvrc