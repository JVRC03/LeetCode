class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        f = len(nums) - 1

        while f > -1:
            nums.append(nums[f])
            f -= 1

        return nums
        