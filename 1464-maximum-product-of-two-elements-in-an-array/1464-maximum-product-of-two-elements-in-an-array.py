class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f, r = 0, 0

        for i in range(len(nums)):
            if nums[i] >= r:
                f = r
                r = nums[i]
            else:
                f = max(f, nums[i])
        
        return (f - 1) * (r - 1)
        