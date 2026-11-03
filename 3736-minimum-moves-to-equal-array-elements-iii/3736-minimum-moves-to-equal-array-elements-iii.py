class Solution:
    def minMoves(self, nums: List[int]) -> int:
        k = max(nums)
        jvrc = 0

        for i in range(len(nums)):
            jvrc += abs(nums[i]-k)

        return jvrc
        