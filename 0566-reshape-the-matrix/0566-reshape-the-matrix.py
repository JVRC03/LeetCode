class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        a = len(mat) * len(mat[0])
        b = r * c

        if a != b:
            return mat
        
        jvrc = []
        temp = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])

                if len(temp) == c:
                    jvrc.append(temp)
                    temp = []
        
        return jvrc

        