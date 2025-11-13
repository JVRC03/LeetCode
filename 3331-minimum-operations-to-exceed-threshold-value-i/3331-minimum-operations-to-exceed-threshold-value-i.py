class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        jvrc = 0

        for i in range(len(nums)):
            if nums[i] < k:
                jvrc += 1
        
        return jvrc
        