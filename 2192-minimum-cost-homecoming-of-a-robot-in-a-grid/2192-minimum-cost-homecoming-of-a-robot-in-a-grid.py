class Solution:
    def minCost(self, x: List[int], y: List[int], a: List[int], b: List[int]) -> int:
        jvrc = 0

        if x[0] <= y[0]:
            for i in range(x[0]+1, y[0]+1):
                jvrc += (a[i])
        else:
            for i in range(x[0]-1, y[0]-1, -1):
                jvrc += a[i]

        if x[1] <= y[1]:
            for i in range(x[1]+1, y[1]+1):
                jvrc += (b[i])
        else:
            for i in range(x[1]-1, y[1]-1, -1):
                jvrc += b[i]
        
        return jvrc