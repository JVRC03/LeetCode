class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot, curr = 0, 0

        for i in range(len(nums)):
            s = str(nums[i])
            tot += nums[i]

            for j in range(len(s)):
                curr += int(s[j])
        
        return abs(tot - curr)
        