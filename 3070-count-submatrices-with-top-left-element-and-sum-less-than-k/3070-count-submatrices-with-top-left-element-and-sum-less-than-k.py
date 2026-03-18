class Solution:
    def countSubmatrices(self, mat: List[List[int]], target: int) -> int:
        jvrc = 0       
        top = []

        for i in range(len(mat)):
            temp = []
            local = 0
            for j in range(len(mat[0])):
                local += mat[i][j]
                val = -1

                if len(top):
                    val = local + top[i-1][j]
                else:
                    val = local

                temp.append(val)

                if val <= target:
                    jvrc += 1
                else:
                    break

            top.append(temp)
                
        return jvrc