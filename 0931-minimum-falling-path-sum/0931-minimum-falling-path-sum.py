class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        dp = mat[-1]

        for i in range(len(mat) - 2, -1, -1):
            curr = []
            for j in range(len(mat[i])):
                a, b, c = float('inf'), dp[j], float('inf')

                if j - 1 >= 0:
                    a = dp[j - 1]
                if j + 1 < len(mat[i]):
                    c = dp[j + 1]
                
                curr.append(mat[i][j] + min(a, b, c))
            
            dp = curr
    
        return min(dp)

        