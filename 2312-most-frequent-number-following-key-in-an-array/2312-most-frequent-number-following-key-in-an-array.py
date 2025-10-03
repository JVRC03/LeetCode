class Solution:
    def mostFrequent(self, nums: List[int], k: int) -> int:
        dic = {}
        jvrc = 0
        curr = 0

        for i in range(len(nums)-1):
            if nums[i] == k:
                if nums[i+1] not in dic:
                    dic[nums[i+1]] = 1
                else:
                    dic[nums[i+1]] += 1
            
                if curr < dic[nums[i+1]]:
                    curr = dic[nums[i+1]]
                    jvrc = nums[i+1]

        return jvrc

            

        