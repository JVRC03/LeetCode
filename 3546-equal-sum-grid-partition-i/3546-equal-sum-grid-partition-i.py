class Solution:
    def canPartitionGrid(self, mat: List[List[int]]) -> bool:

        def rotate(mat):
            temp = []
            for i in range(len(mat[0])):
                k = []
                for j in range(len(mat)):
                    k.append(mat[j][i])
                temp.append(k)
            
            return temp
        
        def check(mat):
            p_sum = []

            for i in range(len(mat)):
                temp = []
                for j in range(len(mat[0])):
                    if not len(temp):
                        temp.append(mat[i][j])
                    else:
                        temp.append(temp[-1] + mat[i][j])
                p_sum.append(temp)
            
            arr = []

            for i in range(len(mat)):
                if not len(arr):
                    arr.append(p_sum[i][-1])
                else:
                    arr.append(arr[-1] + p_sum[i][-1])
            
            for i in range(1, len(arr)):
                if arr[i-1] == arr[-1]-arr[i-1]:
                    return True
            
            return False

        if check(mat):
            return True

        mat = rotate(mat)

        return check(mat)
        