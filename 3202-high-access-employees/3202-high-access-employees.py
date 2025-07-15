class Solution:
    def findHighAccessEmployees(self, a: List[List[str]]) -> List[str]:
        dic = {}

        def f(s):
            h = (((int(s[0])*10)+(int(s[1])))*60)
            m = (int(s[2])*10) + int(s[3])

            return h+m

        for i in range(len(a)):
            if a[i][0] not in dic:
                dic[a[i][0]] = [f(a[i][1])]
            else:
                dic[a[i][0]].append(f(a[i][1]))        
            
        jvrc = []

        for i in dic:
            arr = dic[i]

            if len(arr) < 3:
                continue
            arr.sort()

            for k in range(len(arr)-2):
                if arr[k+2]-arr[k] < 60:
                    jvrc.append(i)
                    break

        return jvrc