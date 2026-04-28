class Solution:
    def minOperations(self, mat: List[List[int]], x: int) -> int:
        arr = []
        curr = mat[0][0] % x

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] % x != curr:
                    return -1
                arr.append(mat[i][j])
        
        arr.sort()
        val = arr[len(arr)//2]

        jvrc = 0

        for i in range(len(arr)):
            diff = abs(arr[i] - val)
            jvrc += (diff // x)

        return jvrc            
        
        