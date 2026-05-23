class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        f, r = 0, len(nums) - 1
        jvrc = 0
        
        while f < r:
            if nums[r] == 0:
                r -= 1
                continue
            if nums[f] == 0:
                nums[f], nums[r] = nums[r], nums[f]
                jvrc += 1
                r -= 1

            f += 1
        
        return jvrc