class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        l, r = 0, 0
        idx = -1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                l += nums[i]
            else:
                l += nums[i]
                idx = i
                break
        
        for i in range(idx, len(nums)):
            r += nums[i]
        
        if l > r:
            return 0
        
        if r > l:
            return 1
        
        return -1
        

        