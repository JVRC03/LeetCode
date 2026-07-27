class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f, s = 0, 0

        for i in range(len(nums)):
            if nums[i] > f:
                s = f
                f = nums[i]
            elif nums[i] > s:
                s = nums[i]

        return (f - 1) * (s - 1) 
        