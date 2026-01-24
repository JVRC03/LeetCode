class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        jvrc = 0
        nums.sort()

        for i in range(len(nums)//2):
            k = nums[i] + nums[len(nums) - i - 1]

            jvrc = max(jvrc, k)
        
        return jvrc
        