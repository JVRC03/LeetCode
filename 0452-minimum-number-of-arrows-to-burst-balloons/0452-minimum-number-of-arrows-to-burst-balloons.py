class Solution:
    def findMinArrowShots(self, arr: List[List[int]]) -> int:
        if len(arr) <= 1:
            return 1

        arr.sort()
        jvrc = 1

        a, b = float('-inf'), float('inf')
        f, r = 0, 0
        
        while r < len(arr):
            a = arr[r][0]
            b = min(b, arr[r][1])

            if a <= b:
                r += 1
                continue
            
            jvrc += 1
            b = float('inf')

        return jvrc 

        