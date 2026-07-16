class Solution:
    def numIslands(self, mat: List[List[str]]) -> int:

        def dfs(i, j):
            if i >= len(mat) or i < 0 or j >= len(mat[0]) or j < 0 or mat[i][j] == '0':
                return 
            
            mat[i][j] = '0'
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)
            
        jvrc = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == '1':
                    jvrc += 1
                    dfs(i, j)
        
        return jvrc
        