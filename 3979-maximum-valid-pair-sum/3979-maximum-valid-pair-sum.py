class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        p_sum = [nums[-1]]

        for i in range(len(nums)-2, -1, -1):
            p_sum.append(max(nums[i], p_sum[-1]))
        
        p_sum = p_sum[::-1]

        jvrc = 0

        for i in range(len(nums)):
            idx = i + k

            if idx < len(nums):
                tot = p_sum[idx] + nums[i]
                jvrc = max(jvrc, tot)
            else:
                break
        
        return jvrc
        