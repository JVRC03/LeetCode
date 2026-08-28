class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        jvrc = -1
        curr = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < curr:
                jvrc = max(jvrc, curr - nums[i])
                continue
            
            curr = nums[i]
        
        return jvrc

        