class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        jvrc = float('inf')
        dic = {}

        for i in range(len(nums)-1, -1, -1):
            k = str(nums[i])
            k = k[::-1]
            k = int(k)

            if k in dic:
                jvrc = min(jvrc, abs(i - dic[k]))
            
            dic[nums[i]] = i

        if jvrc == float('inf'):
            jvrc = -1

        return jvrc

       