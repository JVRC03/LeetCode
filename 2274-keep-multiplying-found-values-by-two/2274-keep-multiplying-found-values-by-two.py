class Solution:
    def findFinalValue(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == k:
                k *= 2
        
        return k
       



        