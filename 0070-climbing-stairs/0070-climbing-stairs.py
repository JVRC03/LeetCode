class Solution:

    def dfs(self, curr, n, dp):
        if curr == n:
            return 1
        if curr > n:
            return 0
        
        if dp[curr] != -1:
            return dp[curr]
        
        left = self.dfs(curr + 1, n, dp)
        right = self.dfs(curr + 2, n, dp)

        dp[curr] = left + right

        return dp[curr]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        return self.dfs(0, n, dp)

        
        