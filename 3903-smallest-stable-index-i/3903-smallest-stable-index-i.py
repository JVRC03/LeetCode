class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        a, b = [], []
        aa, bb = -1, float('inf')

        for i in range(len(nums)):
            aa = max(aa, nums[i])
            a.append(aa)

            bb = min(bb, nums[len(nums) - i - 1])
            b.append(bb)
        
        b = b[::-1]

        for i in range(len(nums)):
            if a[i] - b[i] <= k:
                return i

        return -1

        