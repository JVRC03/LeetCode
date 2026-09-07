class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        dp = mat[-1]

        for i in range(len(mat) - 2, -1, -1):
            temp = []
            for j in range(len(mat[0])):
                curr = float('inf')
                for k in range(len(mat)):
                    if j != k:
                        curr = min(curr, dp[k])
                
                temp.append(mat[i][j] + curr)
            
            dp = temp

        return min(dp)
        