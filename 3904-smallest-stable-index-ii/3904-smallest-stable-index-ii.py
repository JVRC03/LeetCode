class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        p_sum = [nums[-1]]

        for i in range(len(nums)-2, -1, -1):
            p_sum.append(min(nums[i], p_sum[-1]))
        p_sum = p_sum[::-1]
        
        curr = 0
        for i in range(len(nums)):
            curr = max(curr, nums[i])

            diff = curr - p_sum[i]

            if diff <= k:
                return i

        return -1
        