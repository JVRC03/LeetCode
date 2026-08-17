class Solution:
    def change(self, k: int, arr: List[int]) -> int:
        dp = []

        for i in range(len(arr)):
            dp.append([-1] * (k + 1))

        def func(i, arr, k):
            if i == len(arr):
                if k == 0:
                    return 1
                return 0

            if dp[i][k] != -1:
                return dp[i][k]

            take = 0
            if k - arr[i] >= 0:
                take = func(i, arr, k - arr[i])
            
            not_take = func(i + 1, arr, k)

            dp[i][k] = take + not_take
            return dp[i][k]

        return func(0, arr, k)
        
        