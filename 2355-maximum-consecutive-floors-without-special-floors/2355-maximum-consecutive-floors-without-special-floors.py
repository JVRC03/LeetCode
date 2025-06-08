class Solution:
    def maxConsecutive(self, a: int, b: int, arr: List[int]) -> int:
        arr.sort()

        jvrc = max(arr[0]-a, b-arr[-1])
        
        for i in range(1, len(arr)):
            jvrc = max(jvrc, arr[i]-arr[i-1]-1)
        
        return jvrc

        