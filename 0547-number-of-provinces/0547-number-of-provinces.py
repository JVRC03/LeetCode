class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        self.jvrc = 0

        dic = {}

        for i in range(len(mat)):
            dic[i] = []
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    dic[i].append(j)
        
        vis = [0] * len(mat)

        def dfs(source):
            if vis[source]:
                return
            
            vis[source] = 1
            a = dic[source]

            for i in range(len(a)):
                dfs(a[i])

        for i in range(len(vis)):
            if vis[i] == 0:
                self.jvrc += 1
                dfs(i)
        
        return self.jvrc
        