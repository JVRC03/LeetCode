class Solution:
    def totalNQueens(self, n: int) -> int:
        self.jvrc = 0
        mat = []
        for i in range(n):
            mat.append(['.'] * n)

        def check(i, j):
            f = i - 1
            while f > -1:
                if mat[f][j] == 'Q':
                    return False
                f -= 1
            
            f, r = i - 1, j - 1
            while f >= 0 and r >= 0:
                if mat[f][r] == 'Q':
                    return False
                
                f -= 1
                r -= 1
            
            f, r = i - 1, j + 1
            while f > -1 and r < len(mat[0]):
                if mat[f][r] == 'Q':
                    return False
                
                f -= 1
                r += 1
            
            return True

        def func(idx):
            if idx >= len(mat):
                self.jvrc += 1
                return 

            for i in range(len(mat)):
                mat[idx][i] = 'Q'
                if check(idx, i):
                    func(idx + 1)
                mat[idx][i] = '.'

        func(0)
        return self.jvrc
        