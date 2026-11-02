class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]

        jvrc = 0
        for i in range(len(nums)):
            jvrc += abs(nums[i] - mid)
        
        return jvrc