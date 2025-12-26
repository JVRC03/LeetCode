class Solution:
    def minProcessingTime(self, a: List[int], arr: List[int]) -> int:
        jvrc = 0
        a.sort()
        a = a[::-1]

        arr.sort()

        while len(arr):
            k = a[-1]+arr[-1]
            a.pop()
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()

            jvrc = max(jvrc, k)
        
        return jvrc
        