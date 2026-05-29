class Solution:
    def minElement(self, nums: List[int]) -> int:
        jvrc = float('inf')

        for i in range(len(nums)):
            temp = nums[i]
            curr = 0

            while temp:
                curr += (temp % 10)
                temp //= 10
            
            jvrc = min(jvrc, curr)
        
        return jvrc