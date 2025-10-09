class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            k = 0
            for j in range(len(s)):
                k += int(s[j])
            
            if k == i:
                return i
        
        return -1
        