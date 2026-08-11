class Solution:
    def stoneGame(self, arr: List[int]) -> bool:
        dp = []

        for i in range(len(arr)):
            temp = [-1] * len(arr)
            dp.append(temp)

        def func(i, j, arr, alice):
            if i == j:
                return arr[i]
            
            if dp[i][j] != -1:
                return dp[i][j]

            left, right = -1, -1
            if alice:
                left = arr[i] + func(i + 1, j, arr, 0)
                right = arr[j] + func(i, j - 1, arr, 0)
            else:
                left = arr[i] + func(i + 1, j, arr, 1)
                right = arr[j] + func(i, j - 1, arr, 1)
            
            dp[i][j] = max(left, right)
            return dp[i][j]

        tot = func(0, len(arr) - 1, arr, 1)

        if tot > sum(arr) - tot:
            return True

        return False
        