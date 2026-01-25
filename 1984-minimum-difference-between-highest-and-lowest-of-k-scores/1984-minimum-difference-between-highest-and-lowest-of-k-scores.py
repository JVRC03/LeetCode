class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        jvrc = float('inf')
        nums.sort()

        f, r = 0, k-1

        while f <= r and r < len(nums):
            diff = nums[r] - nums[f]

            jvrc = min(jvrc, diff)

            f += 1
            r += 1
        
        return jvrc

        