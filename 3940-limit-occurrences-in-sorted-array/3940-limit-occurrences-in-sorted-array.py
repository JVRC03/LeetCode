class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        jvrc, curr, val = [], -1, -1

        i = 0
        while i < len(nums):
            if val == -1:
                val = nums[i]
                curr = 1
                if curr <= k:
                    jvrc.append(val)
                i += 1
            else:
                if val == nums[i]:
                    curr += 1
                else:
                    val = nums[i]
                    curr = 1
                
                if curr <= k:
                    jvrc.append(val)
                i += 1
                
        return jvrc


        