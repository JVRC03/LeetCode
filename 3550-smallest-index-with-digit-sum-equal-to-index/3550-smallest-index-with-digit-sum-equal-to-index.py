class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            curr = 0
            while nums[i]:
                curr += (nums[i] % 10)
                nums[i] //= 10
            
            if curr == i:
                return i
        
        return -1

        