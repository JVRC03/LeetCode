class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        z, o = 0, 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                z += 1
            else:
                o += 1
        
        for i in range(z):
            nums[i] = 0
        for i in range(z, len(nums)):
            nums[i] = 1
        
        return nums
        