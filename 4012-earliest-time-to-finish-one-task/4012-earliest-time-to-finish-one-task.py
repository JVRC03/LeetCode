class Solution:
    def earliestTime(self, arr: List[List[int]]) -> int:
        jvrc = float('inf')

        for i in range(len(arr)):
            k = arr[i][0]+arr[i][1]

            jvrc = min(jvrc, k)
        
        return jvrc
        