class Solution:
    def minSwaps(self, mat: List[List[int]]) -> int:
        arr = []

        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] == 1:
                    break
                c += 1
            
            arr.append(c)

        jvrc = 0
        c = len(mat)-1

        for i in range(len(arr)):
            if c <= arr[i]:
                c -= 1
                continue
            idx = -1
            for j in range(i+1, len(arr)):
                if arr[j] >= c:
                    idx = j
                    break

            if idx == -1:
                return -1
            temp = arr[idx]

            for j in range(idx, i, -1):
                arr[j] = arr[j-1]
                jvrc += 1
            
            arr[i] = temp
            c -= 1
        
        
        return jvrc
        