class Solution:
    def findRotation(self, ma: List[List[int]], target: List[List[int]]) -> bool:
        self.mat = []

        for i in range(len(ma)):
            g=[]
            for j in range(len(ma)):
                g.append(ma[i][j])
            self.mat.append(g)

        def rotate(target):
            for i in range(len(self.mat)):
                for j in range(i+1, len(self.mat)):
                    self.mat[i][j], self.mat[j][i] = self.mat[j][i], self.mat[i][j]
                
                f, r = 0, len(self.mat)-1
                
                while f < r:
                    self.mat[i][f], self.mat[i][r] = self.mat[i][r], self.mat[i][f]
                    f += 1
                    r -= 1
            
            for i in range(len(self.mat)):
                for j in range(len(self.mat)):
                    if self.mat[i][j] != target[i][j]:
                        return False
            
            return True

        for i in range(4):
            if rotate(target):
                return True

        return False
        
        