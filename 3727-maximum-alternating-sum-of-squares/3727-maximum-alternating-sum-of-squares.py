class Solution:
    def maxAlternatingSum(self, nums: List[int]):
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
            
        nums.sort()
        jvrc = 0
        f, r = 0, len(nums) - 1

        while f <= r:
            jvrc += (nums[r] * nums[r])
            if f != r:
                jvrc -= (nums[f] * nums[f])
            
            f += 1
            r -= 1

        return jvrc
        