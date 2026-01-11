class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(len(nums)):
            s = set()
            curr = 0
            for j in range(i, len(nums)):
                s.add(nums[j])
                curr += nums[j]

                if curr in s:
                    jvrc += 1
        
        return jvrc
        