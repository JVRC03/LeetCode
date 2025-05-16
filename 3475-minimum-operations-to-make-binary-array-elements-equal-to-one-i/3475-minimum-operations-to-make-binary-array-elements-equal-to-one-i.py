class Solution:
    def minOperations(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(len(nums)-2):
            if nums[i] == 0:
                jvrc += 1
                nums[i+1] = abs(nums[i+1]-1)
                nums[i+2] = abs(nums[i+2]-1)
        
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        
        return jvrc
        