class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        jvrc, curr = 0, 0

        for i in range(len(nums)):
            if minK <= nums[i] <= maxK:
                curr += 1
                continue
            
            n = curr
            jvrc += ((n * (n + 1)) // 2)
            curr = 0
        
        n = curr
        jvrc += ((n * (n + 1)) // 2)
        
        return jvrc
        

        