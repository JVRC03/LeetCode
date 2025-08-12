class Solution:
    def canChoose(self, arr: List[List[int]], nums: List[int]) -> bool:
        
        f, i = 0, 0
        while i < len(nums):
            if f >= len(arr):
                return True
            if arr[f][0] == nums[i]:
                c = 0
                for j in range(len(arr[f])):
                    if (i+j) < len(nums) and arr[f][j] == nums[i+j]:
                        c += 1
                        continue
                    break
                
                if c == len(arr[f]):
                    f += 1
                    i += c
                else:
                    i += 1
            else:
                i += 1
            
        if f >= len(arr):
            return True

        return False


       

        

        