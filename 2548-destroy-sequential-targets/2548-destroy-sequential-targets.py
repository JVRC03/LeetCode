class Solution:
    def destroyTargets(self, nums: List[int], k: int) -> int:
        jvrc, curr = float('inf'), 0
        dic = {}

        for i in range(len(nums)):
            temp = nums[i]%k
            if temp not in dic:
                dic[temp] = [1, nums[i]]
            else:
                dic[temp][0] += 1
                dic[temp][1] = min(dic[temp][1], nums[i])
        
        for i in dic:
            if dic[i][0] > curr:
                curr = dic[i][0]
                jvrc = dic[i][1]
            elif dic[i][0] == curr:
                jvrc = min(jvrc, dic[i][1])
        
        return jvrc

      