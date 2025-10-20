class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        jvrc = 0
        maxi, curr = nums[0], nums[-1]
        r_max = []

        for i in range(len(nums)-1, 0, -1):
            r_max.append(curr)
            curr = min(curr, nums[i])
        
        r_max.append(-1)
        r_max = r_max[::-1]

        for i in range(1, len(nums)-1):
            if maxi < nums[i] < r_max[i]:
                jvrc += 2

            elif nums[i-1] < nums[i] < nums[i+1]:
                jvrc += 1
                
            maxi = max(maxi, nums[i])

        return jvrc

            
        