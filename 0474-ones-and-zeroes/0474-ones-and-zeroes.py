class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        arr = []

        for i in range(len(s)):
            temp = s[i]
            o, z = 0, 0
            for j in range(len(temp)):
                if temp[j] == '1':
                    o += 1
                else:
                    z += 1
                
            arr.append([z, o])
        
        dp = []
        for i in range(len(arr)):
            temp = []
            for j in range(m + 1):
                temp.append([-1] * (n + 1))
            
            dp.append(temp)

        def func(i, arr, m, n):
            if i >= len(arr):
                return 0

            if dp[i][m][n] != -1:
                return dp[i][m][n]

            take = 0
            if m - arr[i][0] >= 0 and n - arr[i][1] >= 0:
                take = 1 + func(i + 1, arr, m - arr[i][0], n - arr[i][1])
            
            not_take = func(i + 1, arr, m, n)

            dp[i][m][n] = max(take, not_take)
            return dp[i][m][n]

        return func(0, arr, m, n)
        