class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        jvrc = float('inf')

        for i in range(0, len(nums), 2):
            a = str(nums[i])
            b = str(nums[i + 1])

            jvrc = min(jvrc, int(a + b))
        
        return jvrc
        