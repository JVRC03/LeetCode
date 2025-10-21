class Solution:
    def findChampion(self, n: int, arr: List[List[int]]) -> int:
        v = [0] * n
        dic = {}

        for i in range(len(arr)):
            if arr[i][0] not in dic:
                dic[arr[i][0]] = [arr[i][-1]]
            else:
                dic[arr[i][0]].append(arr[i][-1])
        
        def dfs(source):
            if v[source]:
                return
            
            v[source] = 1
            if source not in dic:
                return
            a = dic[source]

            for i in range(len(a)):
                dfs(a[i])

        for i in range(n):
            v = [0] * n
            dfs(i)
            k = v.count(1)
           
            if k == n:
                return i
    
        return -1


        