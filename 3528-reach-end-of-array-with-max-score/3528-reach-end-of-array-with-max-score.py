class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        curr, val = 0, nums[0]
        jvrc = 0

        for i in range(1, len(nums)):
            if nums[i] >= val:
                k = i-curr
                jvrc += (k * nums[curr])
                val = nums[i]
                curr = i
        
        if curr != len(nums)-1:
            jvrc += ((len(nums)-1-curr) * nums[curr])
        
        return jvrc
        