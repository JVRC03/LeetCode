class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a, b = 0, 0

        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                a += 1
            
            if nums[i] >= nums[i+1]:
                b += 1
        
        if a == len(nums)-1 or b == len(nums)-1:
            return True
        
        return False
        