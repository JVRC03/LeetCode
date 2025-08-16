class Solution:
    def maximalNetworkRank(self, n: int, arr: List[List[int]]) -> int:
        dic = {}
        arr.sort()
        for i in range(len(arr)):
            if arr[i][0] not in dic:
                dic[arr[i][0]] = {arr[i][1]}
            else:
                dic[arr[i][0]].add(arr[i][1])
            
            if arr[i][1] not in dic:
                dic[arr[i][1]] = {arr[i][0]}
            else:
                dic[arr[i][1]].add(arr[i][0])
        
        jvrc = 0

        a = list(dic.keys())

        for i in range(len(a)):
            for j in range(i+1, len(a)):
                k = set()
                temp = set()
                    
                for p in dic[a[i]]:
                    k.add(p)
                for p in dic[a[j]]:
                    temp.add(p)
                    
                if a[i] in temp:
                    k.remove(a[j])

                jvrc = max(jvrc, len(k)+len(temp))
        
        return jvrc        