class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic = {}
        jvrc = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] not in dic:
                    dic[nums[i][j]] = 1
                else:
                    dic[nums[i][j]] += 1
                
                if dic[nums[i][j]] == len(nums):
                    jvrc.append(nums[i][j])
        
        jvrc.sort()
        return jvrc
        