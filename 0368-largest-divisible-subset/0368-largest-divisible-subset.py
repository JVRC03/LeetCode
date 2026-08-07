class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr.sort()
        dp = [1] * len(arr)
        idx = [i for i in range(len(arr))]
        glob = -1

        for i in range(len(arr)):
            curr = 1
            for j in range(i):
                if arr[i] % arr[j] == 0 or arr[j] % arr[i] == 0:
                    if curr < 1 + dp[j]:
                        curr = 1 + dp[j]
                        idx[i] = j            
            dp[i] = curr

            if dp[i] > glob:
                glob = dp[i]
                index = i

        jvrc = [arr[index]]        

        for i in range(glob-1):
            jvrc.append(arr[idx[index]])
            index = idx[index]

        return jvrc

        