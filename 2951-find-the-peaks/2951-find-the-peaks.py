class Solution:
    def findPeaks(self, nums: List[int]) -> List[int]:
        jvrc = []

        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                jvrc.append(i)
        
        return jvrc
        