class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        jvrc = []
        p_sum = [nums[0]]
        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1] + nums[i])
        
        for i in range(len(nums)):
            left, right = 0, 0

            if i == 0:
                left = 0
                right = p_sum[-1]-p_sum[i]
            elif i == len(nums)-1:
                right = 0
                left = p_sum[-2]
                print(left)
            else:
                left = p_sum[i-1]
                right = p_sum[-1]-p_sum[i]
            
            a = i * nums[i]
            b = (len(nums) - i - 1 )* nums[i]

            x = abs(right - b)
            y = abs(a - left)

            jvrc.append(x+y)

        return jvrc
            

        