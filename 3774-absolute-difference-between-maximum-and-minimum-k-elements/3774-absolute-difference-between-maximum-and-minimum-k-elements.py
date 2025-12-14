class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()        
        jv, rc = 0, 0

        for i in range(k):
            jv += nums[i]
            rc += (nums[len(nums)-i-1])
        
        return abs(jv - rc)
        