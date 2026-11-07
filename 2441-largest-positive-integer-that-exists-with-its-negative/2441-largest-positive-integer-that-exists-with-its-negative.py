class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        s = set()
        jvrc = -1

        for i in range(len(nums)):
            s.add(nums[i])

            if -nums[i] in s:
                jvrc = max(jvrc, abs(nums[i]))
            
        return jvrc
        