class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        p_sum = [nums[0]]

        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1]+nums[i])
        
        jvrc = []

        for i in range(len(nums)):
            k = -1
            if i == 0:
                k = abs(((len(nums)-1)*nums[i])-(p_sum[-1]-p_sum[0]))
            elif i == len(nums)-1:
                k = abs( ((len(nums)-1)*nums[i]) - (p_sum[-2]) )
            else:
                r = abs(((len(nums)-i-1) * nums[i]) - (p_sum[-1]-p_sum[i]))
                l = abs((i * nums[i]) - p_sum[i-1])

                k = (l+r)

            jvrc.append(k)
        
        return jvrc
        