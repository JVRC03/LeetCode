class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        
        curr, prev = 0, 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            
            if arr[i - 1] < arr[i]:
                prev = 1
                if curr:
                    return False
                continue
            
            if arr[i - 1] > arr[i]:
                if prev == 0:
                    return False
                curr = 1
                continue

        if not curr:
            return False
        return True                
        