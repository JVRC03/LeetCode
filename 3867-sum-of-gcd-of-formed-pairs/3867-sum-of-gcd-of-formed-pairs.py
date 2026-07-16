class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        curr_max = float('-inf')
        jvrc = 0
        p_sum = []

        def gcd(a, b):
            if b == 0:
                return a
            
            rem = a % b

            return gcd(max(rem, b), min(rem, b))

        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])
            a, b = max(curr_max, nums[i]), min(curr_max, nums[i])
            p_sum.append(gcd(a, b))
        
        p_sum.sort()

        f, r = 0, len(nums) - 1

        while f < r:
            jvrc += gcd(p_sum[r], p_sum[f])
            f += 1
            r -= 1
        
        return jvrc


        