class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a, b = -1, -1
        mini, maxi = float('inf'), float('-inf')

        for i in range(len(nums)):
            if mini > nums[i]:
                mini = nums[i]
                a = i
            
            if maxi < nums[i]:
                maxi = nums[i]
                b = i
        
        j = max(a, b) + 1
        v = len(nums) - min(a, b)
        rc = (min(a, b) + 1) + (len(nums) - max(a, b))

        return min(j, v, rc)
        