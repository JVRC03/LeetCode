class Solution:
    def countSubIslands(self, mat1: List[List[int]], mat2: List[List[int]]) -> int:

        k = set()

        def dfs(mat1, i, j):
            if i >= len(mat1) or j >= len(mat1[0]) or i < 0 or j < 0 or mat1[i][j] == 0:
                return
            
            k.add((i, j))
            mat1[i][j] = 0

            dfs(mat1, i, j+1)
            dfs(mat1, i, j-1)
            dfs(mat1, i+1, j)
            dfs(mat1, i-1, j)

        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j] == 1:
                    dfs(mat1, i, j)
        
        self.jvrc = 0
        self.temp = []

        def dfs1(mat2, i, j):
            if i >= len(mat2) or j >= len(mat2[0]) or i < 0 or j < 0 or mat2[i][j] == 0:
                return 
            
            self.temp.append((i, j))
            mat2[i][j] = 0

            dfs1(mat2, i, j+1)
            dfs1(mat2, i, j-1)
            dfs1(mat2, i+1, j)
            dfs1(mat2, i-1, j)

        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                if mat2[i][j] == 1:
                    self.temp = []
                    dfs1(mat2, i, j)
                    c = 0

                    for idx in range(len(self.temp)):
                        if self.temp[idx] not in k:
                            break
                        c += 1
                    
                    if c == len(self.temp):
                        self.jvrc += 1
        
        return self.jvrc