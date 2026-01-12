class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        jvrc = float('-inf')
        a, b = 1, 1

        for i in range(len(nums)):
            a *= nums[i]
            b *= nums[len(nums)-i-1]

            jvrc = max(jvrc, a, b)

            if not a:
                a = 1
            if not b:
                b = 1
        
        return jvrc
        