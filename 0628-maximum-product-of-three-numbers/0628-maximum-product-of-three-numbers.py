class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        jvrc = float('-inf')

        for i in range(len(nums)-2):
            curr = nums[i] * nums[i + 1] * nums[i + 2]
            jvrc = max(jvrc, curr)
        
        jvrc = max(jvrc, nums[0] * nums[1] * nums[-1])
        jvrc = max(jvrc, nums[0] * nums[-1] * nums[-2])

        return jvrc
        

        