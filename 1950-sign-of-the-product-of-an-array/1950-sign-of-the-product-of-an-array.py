class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            if not nums[i]:
                return 0
            if nums[i] < 0:
                c += 1
        
        if c%2 == 0:
            return 1
        
        return -1
        