class Solution:
    def alertNames(self, key: List[str], val: List[str]) -> List[str]:
        dic = {}

        for i in range(len(key)):
            e = int(val[i][0:2])
            e = (e*60)
            x = e+int(val[i][3:len(val[i])])

            if key[i] not in dic:
                dic[key[i]] = []
            dic[key[i]].append(x)

        
        jvrc = []
        
        for i in dic:
            arr = dic[i]
            arr.sort()
            success = 0

            for j in range(len(arr)-2):
                if arr[j+2]-arr[j] <= 60:
                    success = 1
                    break
            
            if success:
                jvrc.append(i)           
        
        jvrc.sort()

        return jvrc


                
                
        