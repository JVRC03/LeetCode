class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pre, curr = [], float('inf')

        for i in range(len(nums)-1, -1, -1):
            curr = min(curr, nums[i])
            pre.append(curr)
        
        pre = pre[::-1]

        curr = -1
        for i in range(len(nums)):
            curr = max(curr, nums[i])
            if curr - pre[i] <= k:
                return i
        
        return -1



        