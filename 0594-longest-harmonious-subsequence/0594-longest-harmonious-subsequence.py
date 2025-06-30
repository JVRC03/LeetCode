class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        jvrc = 0

        for i in dic:
            if i+1 in dic:
                jvrc = max(jvrc, (dic[i]+dic[i+1]))
            if i-1 in dic:
                jvrc = max(jvrc, (dic[i]+dic[i-1]))
        
        return jvrc

        