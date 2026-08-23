class Solution:
    def minPathCost(self, mat: List[List[int]], arr: List[List[int]]) -> int:
        dp = mat[-1]

        for i in range(len(mat) - 2, -1, -1):
            curr = []
            for j in range(len(mat[0])):
                val = float('inf')
                idx = mat[i][j]
                for k in range(len(mat[0])):
                    val = min(val, dp[k] + arr[idx][k])
                curr.append(val + idx)
            
            dp = curr

        return min(dp)
        