class Solution:
    def rob(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[-1]

        dp = [-1] * len(arr)

        def f(arr, idx):
            if idx >= len(arr):
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            take = arr[idx] + f(arr, idx + 2)
            not_take = f(arr, idx + 1)

            dp[idx] = max(take, not_take)

            return dp[idx]

        jv = f(arr[0:len(arr)-1], 0)
        dp = [-1] * len(arr)
        rc = f(arr[1:], 0)
        return max(jv, rc)


        