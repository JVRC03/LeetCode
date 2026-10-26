class Solution:
    def __init__(self):
        self.c = 0

    def countIslands(self, mat: List[List[int]], k: int) -> int:
        jvrc = 0

        def dfs(i, j):
            if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or mat[i][j] == 0:
                return 
            
            self.c += mat[i][j]
            mat[i][j] = 0

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]:
                    self.c = 0
                    dfs(i, j)
                    if self.c%k == 0:
                        jvrc += 1
        
        return jvrc

        