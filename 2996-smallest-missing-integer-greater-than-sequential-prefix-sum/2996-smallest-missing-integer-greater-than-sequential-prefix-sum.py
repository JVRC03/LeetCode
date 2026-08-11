class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)

        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                curr += nums[i]
                continue
            break
        
        while curr in s:
            curr += 1

        return curr


        

        