class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = nums.count(0)

        if c > 1:
            return [0] * len(nums)
        
        if c:
            tot = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    tot *= nums[i]
            
            for i in range(len(nums)):
                if nums[i]:
                    nums[i] = 0
                else:
                    nums[i] = tot
            
            return nums
        
        tot = 1
        for i in range(len(nums)):
            tot *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = tot // nums[i]
        
        return nums
            

        