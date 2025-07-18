class Solution:
    def minRectanglesToCoverPoints(self, arr: List[List[int]], w: int) -> int:
        arr.sort()
        jvrc = 0
        curr = arr[0]
        
        for i in range(len(arr)):
            if curr[0] == arr[i][-2]:
                continue
            if abs(curr[-2]-arr[i][-2]) <= w:
                continue
            jvrc += 1
            curr = arr[i]
        
        jvrc += 1

        return jvrc
        