class Solution:
    def areaOfMaxDiagonal(self, arr: List[List[int]]) -> int:
        curr, jvrc = 0, 0

        for i in range(len(arr)):
            k = math.sqrt((arr[i][0]*arr[i][0]) + (arr[i][1]*arr[i][1]))

            if k > curr:
                curr = k
                jvrc = arr[i][0] * arr[i][1]
            elif k == curr:
                jvrc = max(jvrc, arr[i][0]*arr[i][1])
        
        return jvrc
        