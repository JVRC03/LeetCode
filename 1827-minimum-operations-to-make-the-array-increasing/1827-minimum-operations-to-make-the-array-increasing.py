class Solution:
    def minOperations(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                continue
            
            val = (nums[i - 1] - nums[i] + 1)
            jvrc +=val

            nums[i] += val
        
        return jvrc
        