class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(len(nums)):
            k = nums[i]%3

            if k:
                jvrc += min(k, 3-k)
        
        return jvrc