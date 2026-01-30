class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        f, r = 0, len(nums)-1
        jvrc = 0

        while f <= r:
            if f == r:
                jvrc += nums[f]
                break
            
            jvrc += int(str(nums[f])+str(nums[r]))

            f += 1
            r -= 1
        
        return jvrc
        