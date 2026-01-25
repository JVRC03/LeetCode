class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        jvrc = -1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                continue
            
            jvrc = i
            break
        
        return jvrc+1

        