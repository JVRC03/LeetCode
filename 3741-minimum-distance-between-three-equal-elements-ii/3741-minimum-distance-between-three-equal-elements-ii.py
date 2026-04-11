class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = {}
        jvrc = float('inf')
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
            
            arr = dic[nums[i]]

            if len(arr) > 2:
                k = abs(arr[-1] - arr[-2]) + abs(arr[-1] - arr[-3]) + abs(arr[-2] - arr[-3])
                jvrc = min(jvrc, k)

        if jvrc == float('inf'):
            jvrc = -1

        return jvrc       