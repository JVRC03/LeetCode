class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        jvrc = -1
        dic = {}

        for i in range(len(nums) - k + 1):
            
            for j in range(i, i + k):
                if nums[j] not in dic:
                    dic[nums[j]] = [1, i]
                else:
                    if i == dic[nums[j]][-1]:
                        continue
                    dic[nums[j]][0] += 1
            
        for i in dic:
            if dic[i][0] == 1:
                jvrc = max(jvrc, i)
        
        return jvrc


            

            

        
        