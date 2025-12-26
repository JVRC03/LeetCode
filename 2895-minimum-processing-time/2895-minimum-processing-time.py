class Solution:
    def minProcessingTime(self, a: List[int], arr: List[int]) -> int:
        jvrc, f = 0, 0
        a.sort()
    
        arr.sort()

        while len(arr):
            k = a[f]+arr[-1]
            f += 1
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()

            jvrc = max(jvrc, k)
        
        return jvrc
        