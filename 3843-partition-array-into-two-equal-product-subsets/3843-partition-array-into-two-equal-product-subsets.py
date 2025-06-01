class Solution:

    def __init__(self):
        self.tot = 0
        self.jvrc = False
    
    def f(self, nums, idx, curr, k):

        if self.jvrc:
            return 

        if curr == self.tot//curr == k:
            self.jvrc = True
            return
        
        for i in range(idx, len(nums)):
            curr *= nums[i]
            self.f(nums, i+1, curr, k)
            curr //= nums[i]

    def checkEqualPartitions(self, nums: List[int], k: int) -> bool:
        self.tot = 1
        for i in range(len(nums)):
            self.tot *= nums[i]
        
        self.f(nums, 0, 1, k)

        return self.jvrc
        