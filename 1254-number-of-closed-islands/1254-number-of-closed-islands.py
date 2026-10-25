class Solution:
    def closedIsland(self, m: list[list[int]]) -> int:
        self.mat = []

        for i in range(len(m)):
            self.mat.append(m[i])

        def dfs(i, j):
            if i < 0 or i >= len(self.mat) or j < 0 or j >= len(self.mat[0]):
                return 
            
            if self.mat[i][j] == 1 or self.mat[i][j] == '#':
                return 
            
            self.mat[i][j] = '#'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        

        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if i == 0 or i == len(self.mat) - 1 or j == 0 or j == len(self.mat[0]) - 1:
                    if self.mat[i][j] == 0:
                        dfs(i, j)

        jvrc = 0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if self.mat[i][j] == 0:
                    jvrc += 1
                    dfs(i, j)
                    
        
        return jvrc
        