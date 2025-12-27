class Solution:
    def minProcessingTime(self, a: List[int], arr: List[int]) -> int:
        jvrc, fa = 0, 0
        a.sort()
    
        arr.sort()

        while len(arr):
            k = a[fa]+arr[-1]
            fa += 1
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()

            jvrc = max(jvrc, k)
        
        return jvrc
        