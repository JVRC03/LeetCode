class Solution:
    def findMin(self, nums):

        f, r = 0, len(nums) - 1

        while f < r:

            mid = f + (r - f) // 2

            # right side sorted
            if nums[mid] < nums[r]:
                r = mid

            # minimum on right
            elif nums[mid] > nums[r]:
                f = mid + 1

            # duplicates
            else:
                r -= 1

        return nums[f]