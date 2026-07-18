class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = float('inf'), float('-inf')

        for i in range(len(nums)):
            a = min(a, nums[i])
            b = max(b, nums[i])
        
        def gcd(a, b):
            if b == 0:
                return a
            
            rem = a % b

            return gcd(max(b, rem), min(b, rem))

        return gcd(b, a)
      
        