class Solution:
    def getMaximumXor(self, nums: List[int], m: int) -> List[int]:
        maxi = int(math.pow(2, m))-1
        jvrc = []

        for i in range(1, len(nums)):
            nums[i] = (nums[i]^nums[i-1])
        
        while len(nums):
            jvrc.append(maxi-nums[-1])
            nums.pop()
        
        return jvrc


        