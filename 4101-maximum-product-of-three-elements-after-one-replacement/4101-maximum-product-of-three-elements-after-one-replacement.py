class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = [abs(nums[0]), abs(nums[1]), abs(nums[-1]), abs(nums[-2])]
        a.sort()

        return a[-1]*a[-2]*100000

        