class Solution:
    def targetIndices(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        jvrc = []

        for i in range(len(nums)):
            if nums[i] == k:
                jvrc.append(i)
        
        return jvrc
        