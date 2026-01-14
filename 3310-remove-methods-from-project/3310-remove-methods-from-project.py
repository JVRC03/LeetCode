class Solution:
    def __init__(self):
        self.ok = 0

    def remainingMethods(self, n: int, k: int, arr: List[List[int]]) -> List[int]:
        dic = {}
        jvrc = []

        for i in range(n):
            dic[i] = []

        for i in range(len(arr)):
            dic[arr[i][0]].append(arr[i][-1])
        
        v = [0] * n

        def waste_dfs(source):
            if v[source] == -1:
                return 
            
            v[source] = -1

            temp = dic[source]

            for i in range(len(temp)):
                waste_dfs(temp[i])

        waste_dfs(k)

        def dfs(source):
            if v[source] == -1:
                self.ok = 1


            if v[source] == 1:
                return 
            
            v[source] = 1
            temp = dic[source]

            for i in range(len(temp)):
                dfs(temp[i])

        for i in range(n):
            if v[i] == 0:
                dfs(i)
        
        if self.ok:
            return [i for i in range(n)]
        
        for i in range(n):
            if v[i] == 1:
                jvrc.append(i)
        
        return jvrc

        