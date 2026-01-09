class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        curr, jvrc = 0, 0

        for i in range(len(nums)):
            curr += nums[i]

            if curr == k:
                jvrc += 1
            
            diff = curr - k

            if diff in dic:
                jvrc += (dic[diff])
            
            if curr not in dic:
                dic[curr] = 1
            else:
                dic[curr] += 1
        
        return jvrc
        