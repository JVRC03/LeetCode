class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        jvrc = 0

        for i in dic:
            if dic[i]%k == 0:
                jvrc += (i * dic[i])
        
        return jvrc
        