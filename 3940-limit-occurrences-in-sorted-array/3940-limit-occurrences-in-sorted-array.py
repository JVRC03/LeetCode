class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        jvrc, dic = [], {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
            
            if dic[nums[i]] <= k:
                jvrc.append(nums[i])
        
        return jvrc


        