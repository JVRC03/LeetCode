class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        dp, cnt = [1] * len(arr), [1] * len(arr)

        for i in range(len(arr)):
            curr, count = 1, 1
            for j in range(i):
                if arr[i] > arr[j]:
                    if 1+dp[j] > curr:
                        curr = 1 + dp[j]
                        count = cnt[j]
                    elif 1+dp[j] == curr:
                        count += cnt[j]
            
            dp[i] = curr
            cnt[i] = count
        
        maxi, jvrc = 0, 0

        for i in range(len(arr)):
            if dp[i] > maxi:
                maxi = dp[i]
                jvrc = cnt[i]
            elif dp[i] == maxi:
                jvrc += cnt[i]

        return jvrc

        