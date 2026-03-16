class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        jvrc = float('inf')

        f, r = 0, k-1

        while f <= r and r < len(nums):
            curr = nums[r] - nums[f]
            jvrc = min(jvrc, curr)

            f += 1
            r += 1
        
        return jvrc
            

