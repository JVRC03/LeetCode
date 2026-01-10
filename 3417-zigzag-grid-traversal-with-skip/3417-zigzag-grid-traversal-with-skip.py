class Solution:
    def zigzagTraversal(self, mat: List[List[int]]) -> List[int]:
        jvrc = []
        k = len(mat[0])%2

        for i in range(len(mat)):
            if i%2 == 0:
                for j in range(0, len(mat[i]), 2):
                    jvrc.append(mat[i][j])
            else:
                if not k:
                    for j in range(len(mat[i])-1, -1, -2):
                        jvrc.append(mat[i][j])
                else:
                    for j in range(len(mat[i])-2, -1, -2):
                        jvrc.append(mat[i][j])
        return jvrc