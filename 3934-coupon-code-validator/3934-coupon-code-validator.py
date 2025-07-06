class Solution:
    def validateCoupons(self, arr: List[str], b: List[str], act: List[bool]) -> List[str]:
        dic = {
        "electronics" : [], 
        "grocery"     : [], 
        "pharmacy"    : [], 
        "restaurant"  : []
        }

        s = {"electronics", "grocery", "pharmacy", "restaurant"}

        for i in range(len(arr)):
            stop = 0
            if (act[i] == False) or (b[i] not in s) or (len(arr[i]) == 0):
                continue
            
            for j in range(len(arr[i])):
                if arr[i][j].isdigit() or arr[i][j].isalpha() or (arr[i][j] == '_'):
                    continue
                stop = 1
                break
            
            if not stop:
                dic[b[i]].append(arr[i])
        
        jvrc = []

        for i in dic:
            temp = dic[i]
            temp.sort()
            jvrc.extend(temp)
        
        return jvrc


        