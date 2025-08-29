class Solution:
    def subdomainVisits(self, arr: List[str]) -> List[str]:
        dic = {}

        for i in range(len(arr)):
            s = arr[i].split(' ')
            a = int(s[0])
            b = s[1]
            if '.' in b:
                c = b.split('.')
                
                x = c[-1]
                if x not in dic:
                    dic[x] = a
                else:
                    dic[x] += a
                
                x = c[-2]+'.'+c[-1]
                if x not in dic:
                    dic[x] = a
                else:
                    dic[x] += a

                if len(c) > 2:
                    x = c[0] + '.' + c[1] + '.' + c[2]
                    if x not in dic:
                        dic[x] = a
                    else:
                        dic[x] += a

                continue                
                
            if b not in dic:
                dic[b] = a
            else:
                dic[b] += a
        



        jvrc = []

        for i in dic:
            jvrc.append(str(dic[i]) + ' ' + i)
        
        return jvrc
        

        