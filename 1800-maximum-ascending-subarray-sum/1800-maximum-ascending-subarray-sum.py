class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        jvrc = 0
        prev = nums[0]-1
        curr = 0

        for i in range(len(nums)):
            if prev < nums[i]:
                curr += nums[i]
                prev = nums[i]
                jvrc = max(jvrc, curr)
            else:
                curr = nums[i]
                prev = nums[i]
                jvrc = max(jvrc, curr)
        
        return jvrc


        