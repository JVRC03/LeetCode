class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        k = len(nums)
        jvrc = 0

        for i in range(k):
            if k%(i+1) == 0:
                jvrc += (nums[i] * nums[i])
        
        return jvrc

        