class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        k = nums[0]
        for i in range(len(nums)):
            k &= nums[i]
        
        if k:
            return 1

        curr = nums[0]
        jvrc = 0

        for i in range(len(nums)):
            curr &= nums[i]

            if curr == k:
                jvrc += 1
                if i+1 < len(nums):
                    curr = nums[i+1]
        
        return jvrc
        