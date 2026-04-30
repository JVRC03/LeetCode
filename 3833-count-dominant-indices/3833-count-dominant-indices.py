class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        p_sum = [nums[-1]]
        curr = nums[-1]
        c = 2
        
        for i in range(len(nums)-2, -1, -1):
            curr += nums[i]
            temp = curr / c
            c += 1
            p_sum.append(temp)

        p_sum = p_sum[::-1]
        jvrc = 0
        
        for i in range(len(nums)-1):
            if nums[i] > p_sum[i+1]:
                jvrc += 1

        return jvrc
            
        