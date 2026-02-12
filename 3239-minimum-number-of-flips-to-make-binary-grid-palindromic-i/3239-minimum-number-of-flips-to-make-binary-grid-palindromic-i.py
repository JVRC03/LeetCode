class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:

        def jv(mat):
            curr = 0

            for i in range(len(mat)):
                f, r = 0, len(mat[i])-1

                while f < r:
                    if mat[i][f] == mat[i][r]:
                        f += 1
                        r -= 1
                        continue
                    
                    f += 1
                    curr += 1
                    r -= 1
            
            return curr

        def rc(mat):
            curr = 0

            for i in range(len(mat[0])):
                f, r = 0, len(mat)-1

                while f < r:
                    if mat[f][i] == mat[r][i]:
                        f += 1
                        r -= 1
                        continue
                    
                    f += 1
                    curr += 1
                    r -= 1
            
            return curr

        return min( jv(mat), rc(mat))
        