class Solution:
    def colorBorder(self, mat: List[List[int]], r: int, c: int, k: int):
        
        temp = copy.deepcopy(mat)
        arr = set()
        glob = mat[r][c]

        def dfs(i, j, k):
            if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or mat[i][j] == -1 or mat[i][j] != glob:
                return
            
            mat[i][j] = -1
            arr.add((i, j))
            dfs(i+1, j, k)
            dfs(i-1, j, k)
            dfs(i, j-1, k)
            dfs(i, j+1, k)

        dfs(r, c, k)

        arr = list(arr)

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][-1]

            if a == 0 or a == len(mat)-1 or b == 0 or b == len(mat[0])-1:
                mat[a][b] = k
            else:
                if a-1 >= 0 and temp[a-1][b] != glob:
                    mat[a][b] = k
                elif a+1 < len(mat) and temp[a+1][b] != glob:
                    mat[a][b] = k
                elif b-1 >= 0 and temp[a][b-1] != glob:
                    mat[a][b] = k
                elif b+1 < len(mat[0]) and temp[a][b+1] != glob:
                    mat[a][b] = k
                else:
                    mat[a][b] = temp[a][b]

                
        return mat
        