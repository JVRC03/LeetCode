class Solution:
    def countPairs(self, arr: List[str]) -> int:
        dic = {}
        jvrc = 0

        for i in range(len(arr)):
            k = ''

            for j in range(len(arr[i])):
                k += str(ord(arr[i][j])%97)
                k += '-'
            
            if k not in dic:
                dic[k] = 1
            else:
                dic[k] += 1
        
        while len(dic):
            temp = ''
            for i in dic:
                temp = i
                break
            
            x = temp.split('-')
            x.pop()

            a = []
            for i in range(len(x)):
                a.append(int(x[i]))

            for i in range(25):
                k = ''
                for j in range(0, len(a)):
                    k += str((a[j]+1)%26)
                    k += '-'
                    a[j] = (a[j]+1)%26
                
                if (k in dic):
                    jvrc += (dic[k] * dic[temp])
            
            n = dic[temp]-1

            jvrc += ( (n * (n+1))//2 )


            del dic[temp]
        
        return jvrc
            




        