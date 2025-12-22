class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        jvrc = 0
        s = set()

        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                continue
            
            jvrc ^= nums[i]
        
        return jvrc
        