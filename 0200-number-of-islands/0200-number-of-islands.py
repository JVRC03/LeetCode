class Solution:

    def dfs(self, mat, i, j):

        if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or mat[i][j] == '0':
            return
            
        mat[i][j] = '0'    
        
        self.dfs(mat, i+1, j)
        self.dfs(mat, i-1, j)
        self.dfs(mat, i, j+1)
        self.dfs(mat, i, j-1)
                    
                    

    def numIslands(self, mat: List[List[str]]) -> int:
        jvrc = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == '1':
                    jvrc += 1
                    self.dfs(mat, i, j)

        return jvrc
        