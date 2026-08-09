class Solution:
    def maxCoins(self, arr: List[int]) -> int:

        arr.append(1)
        arr.insert(0, 1)

        dp = []
        for i in range(len(arr)):
            temp = [-1] * len(arr)
            dp.append(temp)

        def func(i, j, arr):
            if i > j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            jvrc = 0
            for k in range(i, j+1):
                steps = (arr[i-1] * arr[k] * arr[j+1]) + func(i, k-1, arr) + func(k+1, j, arr)
                jvrc = max(jvrc, steps)
        
            dp[i][j] = jvrc

            return jvrc

        return func(1, len(arr) - 2, arr)
        