class Solution:
    def minSwaps(self, mat: List[List[int]]) -> int:
        arr = []

        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] == 0:
                    c += 1
                    continue
                break
            
            arr.append(c)
        
        k = len(mat)-1
        jvrc = 0

        for i in range(len(arr)):

            if arr[i] >= k:
                k -= 1
                continue
            idx = -1

            for j in range(i, len(arr)):
                if arr[j] >= k:
                    idx = j
                    break
            
            if idx == -1:
                return idx
            temp = arr[idx]

            for j in range(idx, i, -1):
                arr[j] = arr[j-1]
                jvrc += 1
            
            arr[i] = temp
            k -= 1
        
        return jvrc
                
        