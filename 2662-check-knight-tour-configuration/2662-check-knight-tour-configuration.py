class Solution:

    def __init__(self):
        self.curr = 0
        self.s = set()
    
    def f(self, mat, i, j):
        if (i >= len(mat)) or (j >= len(mat)) or i < 0 or j < 0:
            return False
        
        if mat[i][j] == self.curr+1:
            return True

        if i-2 >= 0 and  j+1 < len(mat) and mat[i-2][j+1] == self.curr+1:
            
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i-2][j+1]
            self.f(mat, i-2, j+1)

        elif i-1 >=0 and j+2 < len(mat) and mat[i-1][j+2] == self.curr+1:
            
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i-1][j+2]
            self.f(mat, i-1, j+2)

        elif i+1 < len(mat) and  j+2 < len(mat) and mat[i+1][j+2] == self.curr+1:
           
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i+1][j+2]
            self.f(mat, i+1, j+2)

        elif i+2 < len(mat) and  j+1 < len(mat) and self.curr+1 == mat[i+2][j+1]:
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i+2][j+1]
            self.f(mat, i+2, j+1)

        elif i-2 >= 0 and  j-1 >= 0 and self.curr+1 == mat[i-2][j-1]:
            
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i-2][j-1]
            self.f(mat, i-2, j-1)

        elif i-1 >= 0 and  j-2 >= 0 and self.curr+1 == mat[i-1][j-2]:
            
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i-1][j-2]
            self.f(mat, i-1, j-2)

        elif i+1 < len(mat) and j-2 >= 0 and self.curr+1 == mat[i+1][j-2]:
            
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i+1][j-2]
            self.f(mat, i+1, j-2)
        
        elif i+2 < len(mat) and j-1 >= 0 and self.curr+1 == mat[i+2][j-1]:
            
            self.s.add(self.curr)
            self.s.add(self.curr+1)
            self.curr = mat[i+2][j-1]
            self.f(mat, i+2, j-1)
   
    def checkValidGrid(self, mat: List[List[int]]) -> bool:
        
        self.f(mat, 0, 0)

        if len(mat) < 4:
            return False

        if len(self.s) != len(mat)*len(mat):
            return False

        return True
        