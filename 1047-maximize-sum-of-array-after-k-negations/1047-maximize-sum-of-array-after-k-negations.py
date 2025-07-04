class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        jvrc = 0
        nums.sort()
        mini = float('inf')

        for i in range(len(nums)):

            if abs(nums[i]) < mini:
                mini = abs(nums[i])
            
            if nums[i] < 0:
                if k:
                    k -= 1
                    jvrc += abs(nums[i])
                else:
                    jvrc += nums[i]
            else:
                jvrc += nums[i]
        
        if k%2 == 1:
            jvrc -= (2*mini)
                
        return jvrc
        
        
           
        