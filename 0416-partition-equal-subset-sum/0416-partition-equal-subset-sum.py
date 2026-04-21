class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k = sum(nums) / 2

        if k != int(k):
            return False
        
        k = int(k)
        dp = []

        for i in range(len(nums) + 1):
            temp = [0] * (k + 1)
            temp[0] = 1
            dp.append(temp)
        
        for i in range(1, len(nums) + 1):
            for j in range(nums[i-1]):
                if j >= len(dp[i]):
                    break
                dp[i][j] = dp[i-1][j]
            
            for j in range(nums[i-1], k+1):
                if dp[i-1][j]:
                    dp[i][j] = 1
                    continue
                
                diff = j - nums[i-1]
                if dp[i-1][diff]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

        if dp[-1][-1]:
            return True
        return False


        