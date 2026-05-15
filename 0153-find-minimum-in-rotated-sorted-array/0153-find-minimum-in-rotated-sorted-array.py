class Solution:
    def findMin(self, nums: List[int]) -> int:
        f, r = 0, len(nums) - 1
        jvrc = nums[0]

        while f <= r:
            mid = f + ((r - f) // 2)

            if nums[mid] >= nums[f]:
                jvrc = min(jvrc, nums[f])
                f = mid + 1
            else:
                jvrc = min(jvrc, nums[mid])
                r = mid - 1

        return jvrc