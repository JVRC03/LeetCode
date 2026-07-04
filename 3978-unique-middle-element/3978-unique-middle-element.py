class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        val = nums[len(nums)//2]
        c = 0

        for i in range(len(nums)):
            if nums[i] == val:
                c += 1
        
        if c > 1:
            return False
        
        return True

        