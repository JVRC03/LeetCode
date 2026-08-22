class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = [-1] * len(s)            

        def check(arr, k):
            for i in range(len(arr)):
                if arr[i] == 0:
                    continue
                if arr[i] != k:
                    return 0
            return 1

        def func(idx, s):
            if idx >= len(s):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            glob = float('inf')
            curr = ''
            arr = [0] * 26
            maxi = 0
            
            for i in range(idx, len(s)):
                curr += s[i]
                arr[ord(s[i]) % 97] += 1
                maxi = max(maxi, arr[ord(s[i]) % 97])

                if check(arr, maxi):
                    take = 1 + func(i + 1, s)
                    glob = min(glob, take)

            dp[idx] = glob
            return dp[idx]

        return func(0, s)
        