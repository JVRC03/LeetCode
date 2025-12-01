class Solution:

    def __init__(self):
        self.jvrc = 0
    
    def dfs(self, source, dic, curr, ans):
        
        if len(dic[source]) == 0:
            self.jvrc = max(self.jvrc, curr)
            return 
        
        arr = dic[source]

        for i in range(len(arr)):
            self.dfs(arr[i], dic, curr+ans[source], ans)

    def numOfMinutes(self, n: int, k: int, arr: List[int], ans: List[int]):
        dic = {}

        for i in range(n):
            dic[i] = []
        
        for i in range(len(arr)):
            if arr[i] != -1:
                dic[arr[i]].append(i)
        
        self.dfs(k, dic, 0, ans)

        return self.jvrc
        

        