class Solution:
    def __init__(self):
        self.act = [-1, -1]

    def f(self, mat, i, j):
        if i >= len(mat) or j >= len(mat[0]) or mat[i][j] == 0:
            return 
        
        if mat[i][j] == 1:
            mat[i][j] = 0
            if i >= self.act[0] and j >= self.act[1]:
                self.act[0] = i
                self.act[1] = j
        
        self.f(mat, i, j+1)
        self.f(mat, i+1, j)

    def findFarmland(self, mat: List[List[int]]) -> List[List[int]]:
        jvrc = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr = []
                if mat[i][j] == 1:
                    self.act = [i, j]
                    arr.extend(self.act)
                    self.f(mat, i, j)
                    arr.extend(self.act)
                    jvrc.append(arr)
        
        return jvrc

        