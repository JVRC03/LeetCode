class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) < 4:
            return 0
        
        jvrc = nums[-1]-nums[2]
        jvrc = min(jvrc, nums[-2]-nums[1])
        jvrc = min(jvrc, nums[-3]-nums[0])

        return jvrc 