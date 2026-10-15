class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                jvrc += (len(s) ** 2)
        
        return jvrc
        