class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        jvrc = []

        while len(mat):
            jvrc.extend(mat.pop(0))

            if len(mat):
                i = 0
                while i < len(mat):
                    jvrc.append(mat[i].pop())
                    i += 1
                temp = []

                for i in range(len(mat)):
                    if len(mat[i]):
                        temp.append(mat[i])
                mat = temp
            
            if len(mat):
                c = mat.pop()
                c = c[::-1]
                jvrc.extend(c)
            
            if len(mat):
                i = 0
                c =[]
                while i < len(mat):
                    c.append(mat[i].pop(0))
                    i += 1
                c = c[::-1]
                jvrc.extend(c)

                temp = []

                for i in range(len(mat)):
                    if len(mat[i]):
                        temp.append(mat[i])
                mat = temp               


        return jvrc        




        