class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) <= 1:
                continue
            arr[i+1] = arr[i]+1
        
        return arr[-1]
        