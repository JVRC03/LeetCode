class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a, b = min(nums), max(nums)

        if a+k >= b-k:
            return 0
        
        return (b-k)-(a+k)
        