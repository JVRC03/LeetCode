class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        jvrc = 0

        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                jvrc += (arr[i+1]-arr[i])
        
        return jvrc
        