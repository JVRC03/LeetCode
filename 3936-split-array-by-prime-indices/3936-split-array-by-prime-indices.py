class Solution:
    def splitArray(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        arr[0] = 0
        if len(arr) > 1:
            arr[1] = 0
        
        for i in range(2, int(math.sqrt(len(nums)))+1):
            c = 2*i
            for j in range(c, len(nums), i):
                arr[j] = 0
        
        jv, rc = 0, 0

        for i in range(len(nums)):
            if arr[i]:
                jv += nums[i]
            else:
                rc += nums[i]
        
        return abs(jv-rc)


        