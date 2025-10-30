class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        jvrc = 1
        curr = nums[0]+nums[1]
        i = 2

        while i < len(nums)-1:
            if nums[i]+nums[i+1] == curr:
                jvrc += 1
                i += 1
            else:
                break
            i += 1
        
        return jvrc
        