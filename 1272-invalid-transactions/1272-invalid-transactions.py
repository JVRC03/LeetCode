class Solution:
    def invalidTransactions(self, arr: List[str]) -> List[str]:
        jvrc = []
     
        for i in range(len(arr)):
            k = arr[i].split(',')

            if int(k[2]) > 1000:
                jvrc.append(arr[i])
                continue
            add = 0

            for j in range(len(arr)):
                if i != j:
                    p = arr[j].split(',')
                    if p[0] != k[0]:
                        continue
                    
                    if int(k[2]) > 1000:
                        add = 1
                        break
                    
                    if abs(int(k[1]) - int(p[1])) <= 60 and k[-1] != p[-1]:
                        add = 1
                        break
            
            if add:
                jvrc.append(arr[i])
                     
        return jvrc


             
        