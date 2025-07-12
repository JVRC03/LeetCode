class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        maxi, val = 0, 0

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
            
            if dic[nums[i]] > maxi:
                maxi = dic[nums[i]]
                val = nums[i]

        jvrc = []

        for i in range(maxi):
            jvrc.append([val])

        for i in dic:
            if i == val:
                continue
            
            for j in range(dic[i]):
                jvrc[j].append(i)

        return jvrc



        