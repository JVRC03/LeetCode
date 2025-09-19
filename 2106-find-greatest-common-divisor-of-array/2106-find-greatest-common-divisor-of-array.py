class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = float('inf'), float('-inf')

        for i in range(len(nums)):
            a = min(a, nums[i])
            b = max(b, nums[i])
        
        jvrc = 0

        for i in range(1, b+1):
            if a%i == 0 and b%i == 0:
                jvrc = i
        
        return jvrc
        