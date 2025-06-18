class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        jvrc, i = [], 0

        while i < len(nums):
            temp = [nums[i], nums[i+1], nums[i+2]]

            if temp[1]-temp[0] > k or temp[-1]-temp[0] > k or temp[-1]-temp[1] > k:
                return []
            
            jvrc.append(temp)

            i += 3
        
        return jvrc

        