class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = nums.count(nums[0])
        if a == len(nums):
            return 0
        
        return 1
        