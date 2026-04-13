class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        jvrc = float('inf')

        for i in range(len(nums)):
            if nums[i] == target:
                jvrc = min(jvrc, abs(i - start))
        
        return jvrc
        