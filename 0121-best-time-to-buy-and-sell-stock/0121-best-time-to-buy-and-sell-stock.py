class Solution:
    def maxProfit(self, arr: list[int]) -> int:
        jvrc = 0
        curr = 0

        for i in range(len(arr) - 1, -1, -1):
            curr = max(curr, arr[i])

            jvrc = max(jvrc, curr - arr[i])
        
        return jvrc
        