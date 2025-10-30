class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        curr = nums[0]+nums[1]
        nums[0] = 1
        nums[1] = 2

        while nums[1] < len(nums)-1:
            if nums[nums[1]]+nums[nums[1]+1] == curr:
                nums[0] += 1
                nums[1] += 1
            else:
                break
            nums[1] += 1
        
        return nums[0]
        