class Solution:
    def maxProductPath(self, mat: List[List[int]]) -> int:
        dp = [[mat[-1][-1]]]
        for i in range(len(mat[0]) - 2, -1, -1):
            dp.append([mat[-1][i] * dp[-1][-1]])
        dp = dp[::-1]

        def func(nums, k):
            arr = []
            for i in range(len(nums)):
                arr.append(nums[i] * k)
            
            return arr

        for i in range(len(mat) - 2, -1, -1):
            temp = []
            for j in range(len(mat[0]) - 1, -1, -1):
                curr = []
                if j + 1 < len(mat[0]):
                    curr.extend(func(temp[-1], mat[i][j]))
                
                curr.extend(func(dp[j], mat[i][j]))
                a, b = min(curr), max(curr)
                if a == b:
                    temp.append([a])
                else:
                    temp.append([a, b])
            
            temp = temp[::-1]
            dp = temp.copy()

        ans = max(dp[0])
        if ans < 0:
            return -1

        return ans % 1000000007
        