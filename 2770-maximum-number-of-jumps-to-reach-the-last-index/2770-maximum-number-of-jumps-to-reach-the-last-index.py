class Solution:
    def maximumJumps(self, nums: List[int], k: int) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append([-1] * (len(nums)))

        def func(idx, arr, k, prev):
            if idx == len(arr):
                if prev == len(arr) - 1:
                    return 0
                return float('-inf')

            if dp[idx][prev] != -1:
                return dp[idx][prev]

            glob = -1
            for i in range(idx, len(arr)):
                if -k <= arr[i] - arr[prev] <= k:
                    take = 1 + func(i + 1, arr, k, i)
                    glob = max(glob, take) 

            if glob == -1:
                glob = float('-inf')

            dp[idx][prev] = glob
            return dp[idx][prev]

        val = func(1, nums, k, 0)
        if val == float('-inf'):
            return -1

        return val 

        
        