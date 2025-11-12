class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = len(nums)
        c = 0

        while c < k:
            nums.append(nums[c])
            c += 1
        
        return nums
        