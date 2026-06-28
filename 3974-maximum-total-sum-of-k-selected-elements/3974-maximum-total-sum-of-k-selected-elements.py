class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        jvrc = 0

        while k:
            k -= 1
            curr = nums.pop()

            if curr * mul >= curr:
                jvrc += (curr * mul)
            else:
                jvrc += curr
            
            mul -= 1
        
        return jvrc



        