class Solution:
    def findWinningPlayer(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return nums.index(max(nums))

        arr = []
        curr = nums[0]

        for i in range(len(nums)):
            if curr <= nums[i]:
                curr = nums[i]
                arr.append(i)
        
        jvrc = -1 

        for i in range(len(arr)-1):
            temp = 0
            if i == 0:
                temp = arr[i+1]-arr[i]-1
            else:
                temp = arr[i+1]-arr[i]
            
            if temp >= k:
                jvrc = arr[i]
                break
        
        if jvrc == -1:
            jvrc = arr[-1]

        return jvrc      

        