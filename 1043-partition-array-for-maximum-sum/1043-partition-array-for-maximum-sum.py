class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1] * len(arr)
        
        def func(idx, arr, k):
            if idx >= len(arr):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            glob = 0
            curr = 0
            for i in range(idx, idx + k):
                if i < len(arr):
                    curr = max(curr, arr[i])
                    diff = (curr * (i - idx + 1)) + func(i + 1, arr, k)

                    glob = max(glob, diff)
            
            dp[idx] = glob
            return dp[idx]

        return func(0, arr, k)
        