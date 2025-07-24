class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        mat = [([0] * 10) for i in range(10)]

        for i in range(len(nums)):
            s = str(nums[i])
            for j in range(len(s)):
                mat[j][int(s[j])] += 1
        
        jvrc = 0
        
        while len(mat):
            k = len(nums)

            for i in range(10):
                if mat[-1][i] == 0:
                    continue

                diff = k-mat[-1][i]
                jvrc += (mat[-1][i] * diff)
                k -= mat[-1][i]
             
            mat.pop()
        
        return jvrc





            
        