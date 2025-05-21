class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c = 0
            while nums[i]:
                c += nums[i]%10
                nums[i] //= 10
            if c == i:
                return i
        
        return -1
        