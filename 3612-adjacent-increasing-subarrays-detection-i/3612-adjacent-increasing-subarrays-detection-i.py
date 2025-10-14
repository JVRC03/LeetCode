class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        arr = [0]
        curr = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > curr:
                curr = nums[i]
                continue
            arr.append(i)
            curr = nums[i]

        if len(arr) == 1 and k*2 <= len(nums):
            return True

        for i in range(1, len(arr)-1):
            a = arr[i]-arr[i-1]
            b = arr[i+1]-arr[i]
            
            if k*2 <= a or k*2 <= b:
                return True

            if a >= k and b >= k:
                return True
        
        a = arr[-1]-arr[-2]
        b = len(nums)-arr[-1]

        if (a >= k and b >= k)or k*2 <= a or k*2 <= b:
            return True
        

        return False 


        