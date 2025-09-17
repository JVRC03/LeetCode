class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        arr = []
        for i in nums:
            if i != val:
                c += 1
                arr.append(i)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return c
        