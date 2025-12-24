class Solution:

    def __init__(self):
        self.jvrc = 0
        self.dp = []
    
    def dfs(self, idx, arr, prev):
        if idx >= len(arr):
            return 0

        if self.dp[idx] != float('-inf'):
            return self.dp[idx]
        
        local = 0

        for i in range(idx, len(arr)):
            a = self.dfs(i+1, arr, arr[i][-1])

            if i+1 < len(arr) and arr[idx][-1] < arr[i+1][0]:
                local = max(local, a)

        self.dp[idx] = 1+local
        self.jvrc = max(self.jvrc, self.dp[idx])

        return self.dp[idx]
    
    def findLongestChain(self, arr: List[List[int]]) -> int:
        arr.sort()
        self.dp = [float('-inf')] * len(arr)

        self.dfs(0, arr, float('-inf'))

        return self.jvrc

        