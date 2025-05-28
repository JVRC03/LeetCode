class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        jvrc = 0
        curr = 1
        f, r = 0, 0

        while f <= r and r < len(nums):
            curr *= nums[r]

            if curr >= k:

                while f <= r and curr >= k:
                    n = (r-f)
                    jvrc += (n)
                    curr //= nums[f]
                    f += 1
            r += 1
        
        if curr < k:
            n = r-f
            jvrc += ((n*(n+1))//2)

        return jvrc

        