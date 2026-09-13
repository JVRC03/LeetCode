class Solution:
    def cyclicShift(self, n: int, mat: list[list[int]], row: list[int], col: list[int]):

        def func(nums, n):
            arr = []
            k = n % len(nums)
            for i in range(k - 1, -1, -1):
                arr.append(nums[i])
            
            for i in range(len(nums) - 1, k - 1, -1):
                arr.append(nums[i])
            
            return arr[::-1]

        for i in range(n):
            if row[i]:
                mat[i] = func(mat[i], row[i])
        
        for i in range(n):
            if col[i]:
                arr = []
                for j in range(n):
                    arr.append(mat[j][i])
            
                ans = func(arr, col[i])
                for j in range(n):
                    mat[j][i] = ans[j]
        
        return mat
        