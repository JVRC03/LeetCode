class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        p_sum = [nums[0]]

        for i in range(1, len(nums)):
            p_sum.append(nums[i]+p_sum[-1])
        
        jvrc = float('inf')

        for i in range(l-1, r):
            f = -1
            for j in range(i, len(nums)):
                if f > -1:
                    temp = p_sum[j]-p_sum[f]
                    if temp > 0:
                        if f > -1:
                            jvrc = min(jvrc, temp)
                else:
                    if p_sum[j] > 0:
                        jvrc = min(jvrc, p_sum[j])
                f += 1                

        if jvrc != float('inf'):
            return jvrc

        return -1                    