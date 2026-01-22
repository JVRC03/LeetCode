class Solution:
    def minimumPairRemoval(self, nums: List[int]):
        
        def check(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            
            return True

        jvrc = 0
        while check(nums) == False:
            jvrc += 1
            idx, curr = -1, float('inf')

            for i in range(len(nums)-1):
                k = nums[i] + nums[i+1]

                if k < curr:
                    curr = k
                    idx = i
            nums[idx] = curr
            nums.pop(idx+1)
        
        return jvrc

        