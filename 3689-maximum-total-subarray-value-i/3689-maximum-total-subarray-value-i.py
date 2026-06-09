class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mini, maxi = float('inf'), float('-inf')

        for i in range(len(nums)):
            mini = min(mini, nums[i])
            maxi = max(maxi, nums[i])
        
        return (maxi - mini) * k
        