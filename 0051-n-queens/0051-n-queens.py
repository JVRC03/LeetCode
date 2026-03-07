class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.jvrc = []
        self.ans = []

        for i in range(n):
            temp = ['.'] * n
            self.jvrc.append(temp)

        def test(row, col):

            i, j = row-1, col-1
            while i >= 0 and j >= 0:
                if self.jvrc[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = row-1, col
            while i >= 0:
                if self.jvrc[i][j] == 'Q':
                    return False
                i -= 1
            
            i, j = row-1, col+1
            while i >= 0 and j < len(self.jvrc[0]):
                if self.jvrc[i][j] == 'Q':
                    return False
                
                i -= 1
                j += 1

            return True
            
        def dfs(row, n):
            if row >= n:
                glob = []
                for i in range(len(self.jvrc)):
                    s = ''
                    for j in range(len(self.jvrc)):
                        s += self.jvrc[i][j]
                    glob.append(s)
                
                self.ans.append(glob)
                            
                return
            
            for i in range(n):
                if test(row, i):
                    self.jvrc[row][i] = 'Q'
                    dfs(row+1, n)
                    self.jvrc[row][i] = '.'
                    
        dfs(0, n)
        return self.ans
        