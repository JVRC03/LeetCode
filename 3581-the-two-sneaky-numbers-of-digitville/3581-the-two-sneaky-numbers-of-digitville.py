class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        jvrc = []
        s = set()

        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                jvrc.append(nums[i])
        
        return jvrc
        