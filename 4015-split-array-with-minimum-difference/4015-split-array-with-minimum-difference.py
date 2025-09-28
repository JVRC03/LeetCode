class Solution:
    def splitArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        idx = -1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                l += nums[i]
                continue
            idx = i
            break
        
        if idx == -1:
            return abs(l-nums[-1])

        l += nums[idx]
        
        for i in range(idx+1, len(nums)-1):
            if nums[i] > nums[i+1]:
                r += nums[i]
                continue
                print(2)
            return -1
        r += nums[-1]
        jvrc = abs(l-r)

        if nums[idx] != nums[idx]+1:
            jvrc = min(jvrc, abs(abs(l-nums[idx])-(r+nums[idx])))

        return jvrc
        

        