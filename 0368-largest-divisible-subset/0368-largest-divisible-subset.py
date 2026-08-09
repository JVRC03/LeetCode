class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr.sort()

        dp = [-1] * len(arr)
        has = [i for i in range(len(arr))]

        glob, idx = -1, -1

        for i in range(len(arr)):
            count = 0
            for j in range(i):
                if (arr[j] % arr[i] == 0 or arr[i] % arr[j] == 0) and count < dp[j]:
                    count = dp[j]
                    has[i] = j
            dp[i] = count + 1

            if dp[i] > glob:
                glob = dp[i]
                idx = i
        
        jvrc = [arr[idx]]
        for i in range(glob - 1):
            jvrc.append(arr[has[idx]])
            idx = has[idx]

        return jvrc[::-1]


        