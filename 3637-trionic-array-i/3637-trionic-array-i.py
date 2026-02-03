class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        idx = 0

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                idx += 1
                continue
            break
        
        if idx == len(nums)-1 or idx == 0:
            return False

        temp = idx
        for i in range(idx, len(nums)-1):
            if nums[i] > nums[i+1]:
                idx += 1
                continue
            break
        
        if idx == len(nums)-1 or idx == temp:
            return False
        
        for i in range(idx, len(nums)-1):
            if nums[i] < nums[i+1]:
                idx += 1
                continue
            break
        
        if idx != len(nums)-1:
            return False
        
        return True
        
        
        