class Solution:
    def average(self, arr: List[int]) -> float:
        jvrc, a, b = 0, float('inf'), 0

        for i in range(len(arr)):
            jvrc += arr[i]
            a = min(a, arr[i])
            b = max(b, arr[i])
        
        return (jvrc-a-b)/(len(arr)-2)
        