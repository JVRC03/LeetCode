class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k, idx = -1, -1

        for i in range(len(nums)):
            if nums[i] >= k:
                k = nums[i]
                idx = i

        for i in range(len(nums)):
            if nums[i] != k and 2 * nums[i] > k:
                return -1
        
        return idx
            

        