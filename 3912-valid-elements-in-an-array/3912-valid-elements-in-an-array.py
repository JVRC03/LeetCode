class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums) < 3:
            return nums

        jvrc = []
        jvrc.append(nums[0])
        curr = nums[0]

        p_sum = [nums[-1]]
        jim = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            p_sum.append(jim)

            jim = max(jim, nums[i])
            
        p_sum = p_sum[::-1]
        idx = -1
        
        for i in range(1, len(nums)):
            if nums[i] > curr or nums[i] > p_sum[i]:
                jvrc.append(nums[i])
                idx = i
            
            curr = max(curr, nums[i])
        
        if idx != len(nums)-1:
            jvrc.append(nums[-1])
                
        return jvrc
        