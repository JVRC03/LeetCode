class Solution:
    def findClosestNumber(self, arr: List[int]) -> int:
        diff, jvrc = float('inf'), -1

        for i in range(len(arr)):
            k = abs(0 - arr[i])
            if diff > k:
                jvrc = arr[i]
                diff = k
            elif diff == k:
                jvrc = max(jvrc, arr[i]) 
        
        return jvrc
        